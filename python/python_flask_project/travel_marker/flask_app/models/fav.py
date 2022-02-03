from flask_app.config.mysqlconnection import connectToMySQL
db_name = "users_favorites"

def add_fav(data):
        print(data)
        query1 = "SELECT * FROM favorites WHERE country = %(location)s;"
        results1 = connectToMySQL(db_name).query_db(query1,data)
        print(results1)
        if (results1):
            query = """DELETE FROM favorites WHERE country = %(location)s AND user_id = %(user_id)s
            """
            return connectToMySQL(db_name).query_db(query,data)
        else:
            query = """INSERT INTO favorites (country,user_id,created_at,updated_at) 
            VALUES(%(location)s,%(user_id)s,now(),now())
            """
            return connectToMySQL(db_name).query_db(query,data)

def get_fav(data):
        query = "SELECT country FROM favorites WHERE user_id = %(user_id)s;"
        results = connectToMySQL(db_name).query_db(query,data)
        return results

