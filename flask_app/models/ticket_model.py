from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Ticket:
    def __init__(self, data):
        self.id_ticket = data['id_ticket']
        self.type_service_ticket = data['type_service_ticket']
        self.status_ticket = data['status_ticket']
        self.id_office = data['id_office']
        self.id_client = data['id_client']