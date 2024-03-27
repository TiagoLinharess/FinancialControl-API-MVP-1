from flask import Blueprint, request
from repositories.year import YearRepository
from repositories.month import MonthRepository
from repositories.item import ItemRepository
from models import Session, Year, Month
from schemas.default import DefaultRequestSchema

post_bill_items = Blueprint("post_bill_items", __name__)

# Rota de POST do endpoint de Bill Items
@post_bill_items.post('/bill_items')
def create_bill_item():
    try:
        # Cria sessão
        session = Session()

        # Cria Schema
        schema = read_post_body(request.json)
        
        # Cria ano se não existir
        year = save_year(session, schema.get_year())

        # Cria mês se não existir
        month = save_month(session, schema.get_month(), year)

        # Cria item
        save_item(session, schema.get_name(), schema.get_type(), schema.get_value(), month)

        # Executa commit no banco de dados
        session.commit()

        # Retorno de sucesso da rota
        return { "success": True }, 201
    except Exception as e:
        # Retorno de erro da rota
        return { "error": str(e) }, 400

def read_post_body(content) -> DefaultRequestSchema:
    # Busca body da rota de POST
    year = str(content["year"])
    month = str(content["month"]).lower()
    bill_type = str(content["type"]).lower()
    name = str(content["name"])
    value = float(content["value"])

    # Verifica valor do body
    if not year or not month or not bill_type or not name or not value:
        raise ValueError("Invalid params.")

    # Retornos do schema
    return DefaultRequestSchema(year, month, bill_type, name, value)

def save_year(session: Session, year: str) -> Year:
    try:
        # Instancia repositório
        year_repository = YearRepository(session)

        # Cria ano se existir no repositório
        return year_repository.create(year)
    except Exception as e:
        # Tratativa de erro do repostirório
        raise ValueError("Error on saving year: " + str(e))

def save_month(session: Session, month_string: str, year: Year) -> Month:
    try:
        # Instancia repositório
        month_repository = MonthRepository(session)

        # Cria mês se não existir no repositório
        return month_repository.create(month_string, year)
    except Exception as e:
        # Tratativa de erro do repostirório
        raise ValueError("Error on saving month: " + str(e))

def save_item(session: Session, name: str, type_string: str, value: float, month: Month):
    try:
        # Instancia repositório
        item_repository = ItemRepository(session)

        # Cria item
        item_repository.create(month, name, type_string, value)
    except Exception as e:
        # Tratativa de erro do repostirório
        raise ValueError("Error on saving item: " + str(e))