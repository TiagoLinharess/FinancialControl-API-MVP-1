import json
from models import Year, Month
from typing import List

class DefaultRequestSchema:

    # Inicializa request
    def __init__(self, year: str, month: str):
        self.__year = year
        self.__month = month
    
    # Busca valor de YEAR
    def get_year(self) -> str:
        return self.__year
    
    # Busca valor de MONTH
    def get_month(self) -> str:
        return self.__month

class DefaultResponseSchema:

    # Inicializa response
    def __init__(self, year: Year):
        self.year: str = year.year
        self.months: List[MonthSchema] = list(map(get_month, year.months))
    
    # Transforma objeto em json
    def to_json(self):
        return {
            "year": self.year,
            "months": list(map(get_month_json, self.months))
        }

class MonthSchema:

    # Inicializa response
    def __init__(self, month: Month):
        self.month: str = month.month
    
    # Transforma objeto em json
    def to_json(self):
        return {
            "month": self.month,
            "incomes": [],
            "outcomes": []
        }
    

# Transforma model Month para MonthSchema
def get_month(month: Month) -> MonthSchema:
    return MonthSchema(month)

# Transforma model MonthSchema para Json
def get_month_json(month: Month):
    return MonthSchema(month).to_json()

# Transforma model DefaultResponseSchema para Json
def get_schema_json(year: Year):
    return DefaultResponseSchema(year).to_json()

# Transforma lista Years para Json
def get_default_list(years: List[Year]):
    return list(map(get_schema_json, years))
