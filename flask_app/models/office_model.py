from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Office:
    def __init__(self, data):
        self.id_office = data['id_office']
        self.name_office = data['name_office']
        self.capacity_number = data['capacity_number']
        self.id_district = data['id_district']
        self.latitud_office = data['latitud_office']
        self.longitud_office = data['longitud_office']
