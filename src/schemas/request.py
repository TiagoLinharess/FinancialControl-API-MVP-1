from pydantic import BaseModel
import json
from schemas.month import MonthSchema
from models import Year, Month, Item
from typing import List

class RequestPostSchema(BaseModel):
    year: str
    month: str
    type: str
    name: str
    value: float

class RequestDeleteSchema(BaseModel):
    id: int

class RequestPutSchema(BaseModel):
    id: int
    type: str
    name: str
    value: float

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
