from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Recipe:
    def __init__(self,db_data):
        self.id = db_data["id"]
        self.name = db_data["name"]
        self.description = db_data["description"]
        self.instructions = db_data["instructions"]
        self.under30min = db_data["under30min"]
        self.date_made = db_data["date_made"]
        self.user_id = db_data["user_id"]
        self.created_at = db_data["created_at"]
        self.updated_at = db_data["updated_at"]
        self.user = {}
    db_name = "users_recipes"

    @classmethod
    def add(cls,data):
        query = """INSERT INTO recipes (name,description,instructions,under30min,date_made,user_id,created_at,updated_at) 
        VALUES (%(name)s,%(description)s,%(instructions)s,%(under30min)s,%(date_made)s,%(user_id)s,now(),now());"""
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_recipes = []
        for data in results:
            recipe = cls(data)
            recipe_data = {
                "id" : data["users.id"],
                "first_name" : data["first_name"],
                "last_name" : data["last_name"],
                "email" : data["email"],
                "password" : data["password"],
                "created_at" : data["users.created_at"],
                "updated_at" : data["users.updated_at"]
            }
            recipe.user = user.User(recipe_data)
            all_recipes.append(recipe)
        return all_recipes

    @classmethod
    def update(cls, data):
        query = """UPDATE recipes SET name=%(name)s, description=%(description)s, 
        instructions=%(instructions)s, under30min=%(under30min)s, 
        date_made=%(date_made)s,updated_at=NOW() 
        WHERE id = %(id)s;"""
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate(recipe):
        is_valid = True
        if len(recipe["name"]) < 3:
            is_valid = False
            flash("Name must be at least 3 characters","recipe")
        if len(recipe["instructions"]) < 3:
            is_valid = False
            flash("Instructions must be at least 3 characters","recipe")
        if len(recipe["description"]) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","recipe")
        if recipe["date_made"] == "":
            is_valid = False
            flash("Please enter a date","recipe")
        return is_valid
