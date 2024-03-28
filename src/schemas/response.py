from models import Year
from typing import List
from schemas import DefaultResponseSchema

# Retorno padrão de erro
def get_default_error(exception: str):
    return {
        "error": exception
    }, 400

# Retorno padrão de sucesso
def get_default_success():
    return { "success": True }, 200

# Transforma model DefaultResponseSchema para Json
def get_schema_json(year: Year):
    return DefaultResponseSchema(year).to_json()

# Transforma lista Years para Json
def get_default_list(years: List[Year]):
    return list(map(get_schema_json, years))