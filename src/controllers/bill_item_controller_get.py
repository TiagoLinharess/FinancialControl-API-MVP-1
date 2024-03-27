from flask import Blueprint, request
from repositories.year import YearRepository
from repositories.month import MonthRepository
from repositories.item import ItemRepository
from models import Session, Year, Month, Item
from schemas.default import DefaultResponseSchema, get_default_list
from typing import List

get_bill_items = Blueprint("get_bill_items", __name__)

# Rota de GET do endpoint de Bill Items
@get_bill_items.get('/bill_items')
def read_bill_item():
    try:
        # Cria sessão
        session = Session()

        # Procura anos
        years = get_years(session)

        # Loop para buscar os meses
        for year in years:

            # Procura os meses
            months = get_months(session, year)

            # Atribui meses ao ano
            year.months = months

            # Loop para buscar os items
            for month in months:

                # Atribui items ao mês
                month.items = get_items(session, month)

        return get_default_list(years)
    except Exception as e:
        # Retorno de erro da rota
        return { "error": str(e) }, 400


def get_years(session: Session) -> List[Year]:
    try:
        # Instancia repositório
        year_repository = YearRepository(session)

        # Busca anos se existirem no repositório
        return year_repository.read()
    except Exception as e:
        # Tratativa de erro do repostirório
        raise ValueError("Error on fetching year: " + str(e))

def get_months(session: Session, year: Year) -> List[Month]:
    try:
        # Instancia repositório
        month_repository = MonthRepository(session)

        # Busca meses se existirem no repositório
        return month_repository.read(year)
    except Exception as e:
        # Tratativa de erro do repostirório
        raise ValueError("Error on fetching month: " + str(e))

def get_items(session: Session, month: Month) -> List[Item]:
    try:
        # Instancia repositório
        item_repository = ItemRepository(session)

        # Busca meses se existirem no repositório
        return item_repository.read(month)
    except Exception as e:
        # Tratativa de erro do repostirório
        raise ValueError("Error on fetching items: " + str(e))