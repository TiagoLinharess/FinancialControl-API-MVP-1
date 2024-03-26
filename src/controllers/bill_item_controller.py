from flask import Blueprint, request
from repositories.year import YearRepository
from repositories.month import MonthRepository
from models import Session, Year

bill_items = Blueprint("bill_items", __name__)

@bill_items.post('/bill_items')
def create_bill_item():
    try:
        session = Session()
        content = request.json
        year_string = content['year']
        month_string = content['month'].lower()

        if not year_string or not month_string:
            return { "error": "invalid params" }, 400

        year = save_year(session, year_string)
        save_month(session, month_string, year)
        session.commit()
        return { "success": True }, 201
    except Exception as e:
        return { "error": str(e) }, 400

def save_year(session: Session, year: str) -> Year:
    try:
        year_repository = YearRepository(session)
        return year_repository.create(year)
    except Exception as e:
        raise ValueError("Error on saving year: " + str(e))

def save_month(session: Session, month_string: str, year: Year):
    try:
        month_repository = MonthRepository(session)
        month_repository.create(month_string, year)
    except Exception as e:
        raise ValueError("Error on saving year: " + str(e))