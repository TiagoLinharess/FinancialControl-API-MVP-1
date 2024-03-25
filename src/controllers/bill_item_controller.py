from flask import Blueprint, request
from models import Session, Year

bill_items = Blueprint("bill_items", __name__)

@bill_items.post('/bill_items')
def create_bill_item():
    content = request.json
    year_string = content['year']

    if not year_string:
        return { "error": "param year does not exists" }, 400

    try:
        if exist_year(year_string):
            return { "exist success": True }, 201

        save_year(year_string)
        return { "success": True }, 201
    except Exception as e:
        return { "error": str(e) }, 400

def exist_year(year_string: str):
    try:
        session = Session()
        existent_years = session.query(Year).all()

        for year in existent_years:
            if year.year == year_string:
                return True
        
        return False
    except Exception as e:
        raise ValueError("Error on fetching years:" + str(e))


def save_year(year_string: str):
    try:
        session = Session()
        year = Year(year_string)
        session.add(year)
        session.commit()
    except Exception as e:
        raise ValueError("Error on saving year:" + str(e))