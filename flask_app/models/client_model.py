from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Client:
    def __init__(self, data):
        self.id_client = data['id_client']
        self.id_doc_client = data['id_doc_client']
        self.id_doc_number_doc_clientclient = data['number_doc_client']