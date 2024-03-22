import json

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get('/bill_items')
def get_bill_items():
    return {
        "name": "Conta Luz - Janeiro - 2024",
        "value": 400
    }, 200
