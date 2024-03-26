from flask import Flask, jsonify, request
from models import Session, Year
from routes import api

# Inicializa API
app = Flask(__name__)

# Inicializa rotas
app.register_blueprint(api)


# @app.get('/bill_items')
# def read_bill_item():
#     return {
#         "name": "Conta Luz - Janeiro - 2024",
#         "value": 400
#     }, 200

# @app.post('/bill_items/<int:id>')
# def update_item(id: int):
#     return { "success": True, "id": id }, 201

# @app.delete('/bill_items/<int:id>')
# def delete_item(id: int):
#     return { "success": True, "id": id }, 201
