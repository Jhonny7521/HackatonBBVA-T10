from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class District:
    def __init__(self, data):
        self.id_district = data['id_district']
        self.name_district = data['name_district']
        self.id_city = data['id_city']
