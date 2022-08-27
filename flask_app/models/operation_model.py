from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL


class Operation:
  def __init__(self, data):
    self.id_operation = data['id_operation']
    self.operation_name = data['operation_name']

  @classmethod
  def get_operations(cls):
    query = "SELECT * FROM operations ORDER BY operation_name ASC"
    results = connectToMySQL('db_hackathon').query_db(query)
    print(results)
    return results

