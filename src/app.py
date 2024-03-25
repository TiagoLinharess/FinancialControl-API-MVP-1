import json

from flask import Flask, jsonify, request
from model import Session, Year

app = Flask(__name__)

@app.post('/bill_items')
def create_bill_item():
    content = request.json
    year_string = content['year']

    if not year_string:
        return { "error": "param year does not exists" }, 400

    session = Session()
    existent_years = session.query(Year).all()

    for year in existent_years:
        if year.year == year_string:
            return { "exist success": True }, 201


    try:
        year = Year(year_string)
        session.add(year)
        session.commit()
        return { "success": True }, 201
    except Exception as e:
        return { "error": str(e) }, 400

@app.get('/bill_items')
def read_bill_item():
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
