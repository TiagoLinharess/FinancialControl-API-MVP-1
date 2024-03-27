import json
from models import Year, Month, Item
from typing import List

class DefaultRequestSchema:

    # Inicializa request
    def __init__(self, year: str, month: str, type_string: str, name: str, value: float):
        self.__year = year
        self.__month = month
        self.__type_string = type_string
        self.__name = name
        self.__value = value
    
    # Busca valor de YEAR
    def get_year(self) -> str:
        return self.__year
    
    # Busca valor de MONTH
    def get_month(self) -> str:
        return self.__month
    
    # Busca valor de TYPE
    def get_type(self) -> str:
        return self.__type_string
    
    # Busca valor de NAME
    def get_name(self) -> str:
        return self.__name
    
    # Busca valor de VALUE
    def get_value(self) -> float:
        return self.__value

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
        self.incomes: List[ItemSchema] = get_item_income(month.items)
        self.outcomes: List[ItemSchema] = get_item_outcome(month.items)
    
    # Transforma objeto em json
    def to_json(self):
        return {
            "month": self.month,
            "incomes": list(map(get_item_json, self.incomes)),
            "outcomes": list(map(get_item_json, self.outcomes))
        }

class ItemSchema:

    # Inicializa response
    def __init__(self, item: Item):
        self.name: str = item.name
        self.type: str = item.type
        self.value: str = item.value
    
    # Transforma objeto em json
    def to_json(self):
        return {
            "name": self.name,
            "type": self.type,
            "value": self.value
        }

# Transforma model Item para ItemSchema
def get_item_income(items: List[Item]) -> List[ItemSchema]:
    item_schema: List[ItemSchema] = []

    for item in items:
        if item.type == "income":
            item_schema.append(ItemSchema(item))
    
    return item_schema

# Transforma model Item para ItemSchema
def get_item_outcome(items: List[Item]) -> List[ItemSchema]:
    item_schema: List[ItemSchema] = []

    for item in items:
        if item.type == "outcome":
            item_schema.append(ItemSchema(item))

    return item_schema

# Transforma model ItemSchema para Json
def get_item_json(item: ItemSchema):

    return item.to_json()

# Transforma model Month para MonthSchema
def get_month(month: Month) -> MonthSchema:
    return MonthSchema(month)

# Transforma model MonthSchema para Json
def get_month_json(month: MonthSchema):
    return month.to_json()

# Transforma model DefaultResponseSchema para Json
def get_schema_json(year: Year):
    return DefaultResponseSchema(year).to_json()

# Transforma lista Years para Json
def get_default_list(years: List[Year]):
    return list(map(get_schema_json, years))
