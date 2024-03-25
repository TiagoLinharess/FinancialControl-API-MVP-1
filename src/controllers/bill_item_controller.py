from flask import Blueprint, request
from repositories.year import YearRepository

bill_items = Blueprint("bill_items", __name__)

@bill_items.post('/bill_items')
def create_bill_item():
    content = request.json
    year_string = content['year']

    if not year_string:
        return { "error": "invalid params" }, 400

    try:
        if exist_year(year_string):
            return { "exist success": True }, 201

        save_year(year_string)
        return { "success": True }, 201
    except Exception as e:
        return { "error": str(e) }, 400

def exist_year(year_string: str) -> bool:
    try:
        year_repository = YearRepository()
        existent_years = year_repository.read()

        for year in existent_years:
            if year.year == year_string:
                return True
        
        return False
    except Exception as e:
        raise ValueError("Error on fetching years:" + str(e))


def save_year(year: str):
    try:
        year_repository = YearRepository()
        year_repository.create(year)
    except Exception as e:
        raise ValueError("Error on saving year:" + str(e))