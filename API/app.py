import json

from flask import Flask, jsonify, request
from model import Session

app = Flask(__name__)

@app.post('/bill_items')
def create_bill_item():
    return { "success": True }, 201

@app.get('/bill_items')
def read_bill_item():
    session = Session()

    return {
        "name": "Conta Luz - Janeiro - 2024",
        "value": 400
    }, 200

@app.post('/bill_items/<int:id>')
def update_item(id: int):
    return { "success": True, "id": id }, 201

@app.delete('/bill_items/<int:id>')
def delete_item(id: int):
    return { "success": True, "id": id }, 201
