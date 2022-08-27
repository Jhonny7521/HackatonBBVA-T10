from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class DocumentClient:
    
    def __init__(self, data):
        self.id_doc_client = data['id_doc_client']
        self.type_doc_client = data['type_doc_client']

