from flask import Blueprint, request
from repositories.year import YearRepository
from repositories.month import MonthRepository
from models import Session, Year
from schemas.default import DefaultRequestSchema

get_bill_items = Blueprint("get_bill_items", __name__)

# Rota de POST do endpoint de Bill Items
@get_bill_items.get('/bill_items')
def read_bill_item():
    return {
        "name": "Conta Luz - Janeiro - 2024",
        "value": 400
    }, 200