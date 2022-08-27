from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class City:
    def __init__(self, data):
        self.id_city = data['id_city']
        self.name_city = data['name_city']