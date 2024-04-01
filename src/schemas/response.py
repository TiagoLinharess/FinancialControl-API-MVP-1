from models import Year
from typing import List

# Retorno padrão de erro
def get_default_error(exception: str):
    return {
        "error": exception
    }, 400

# Retorno padrão de sucesso
def get_default_success():
    return { "success": True }, 200