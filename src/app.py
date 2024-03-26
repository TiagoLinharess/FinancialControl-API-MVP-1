from flask import Flask, jsonify, request
from models import Session, Year
from routes import api

# Inicializa API
app = Flask(__name__)

# Inicializa rotas
app.register_blueprint(api)

# @app.post('/bill_items/<int:id>')
# def update_item(id: int):
#     return { "success": True, "id": id }, 201

# @app.delete('/bill_items/<int:id>')
# def delete_item(id: int):
#     return { "success": True, "id": id }, 201
