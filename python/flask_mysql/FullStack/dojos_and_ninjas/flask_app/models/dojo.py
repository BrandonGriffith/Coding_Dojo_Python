from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def list_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def add(cls, data):
        query= """INSERT INTO dojos (name, created_at, updated_at) 
        VALUES (%(name)s, now(), now());"""
        result = connectToMySQL('dojos_ninjas').query_db(query,data)
        return result

    @classmethod
    def get_ninjas(cls, data):
        query = """SELECT * FROM dojos 
        LEFT JOIN ninjas on dojos.id = ninjas.dojo_id 
        WHERE dojos.id = %(id)s;"""
        results = connectToMySQL('dojos_ninjas').query_db(query,data)
        dojo = cls(results[0])
        for info in results:
            ninja = {
                'id': info['ninjas.id'],
                'first_name': info['first_name'],
                'last_name': info['last_name'],
                'age': info['age'],
                'created_at': info['ninjas.created_at'],
                'updated_at': info['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja))
        return dojo
