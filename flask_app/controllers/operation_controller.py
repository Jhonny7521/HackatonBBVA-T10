from flask import request, jsonify
from flask_app import app 

from flask_app.models.operation_model import Operation

@app.route("/api/")
def get_all_operations():
  operations = Operation.get_operations()
  return jsonify(operations)
