from flask import Blueprint, request
from repositories.year import YearRepository
from repositories.month import MonthRepository
from models import Session, Year
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
        
        # Cria Ano se não existir
        year = save_year(session, schema.get_year())

        # Cria mês se não existir
        save_month(session, schema.get_month(), year)

        # Executa commit no banco de dados
        session.commit()

        # Retorno de sucesso da rota
        return { "success": True }, 201
    except Exception as e:
        # Retorno de erro da rota
        return { "error": str(e) }, 400

def read_post_body(content) -> DefaultRequestSchema:
    # Busca body da rota de POST
    year_string = str(content["year"])
    month_string = str(content["month"]).lower()
    
    # Verifica valor do body
    if not year_string or not month_string:
        raise ValueError("Invalid params.")

    # Retornos do schema
    return DefaultRequestSchema(year_string, month_string)

def save_year(session: Session, year: str) -> Year:
    try:
        # Instancia repositório
        year_repository = YearRepository(session)

        # Cria ano se existir no repositório
        return year_repository.create(year)
    except Exception as e:
        # Tratativa de erro do repostirório
        raise ValueError("Error on saving year: " + str(e))

def save_month(session: Session, month_string: str, year: Year):
    try:
        # Instancia repositório
        month_repository = MonthRepository(session)

        # Cria mês se não existir no repositório
        month_repository.create(month_string, year)
    except Exception as e:
        # Tratativa de erro do repostirório
        raise ValueError("Error on saving month: " + str(e))