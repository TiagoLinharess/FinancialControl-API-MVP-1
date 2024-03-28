from flask import Blueprint, request
from repositories import ItemRepository
from models import Session
from schemas import ItemEditSchema, get_default_error, get_default_success

update_bill_items = Blueprint("update_bill_items", __name__)

# Rota de UPDATE do endpoint de Bill Items
@update_bill_items.route("/bill_items", methods=["PUT"])
def update_bill_item():
    try:
        # Cria sessão
        session = Session()

        # Procura campo id no body
        schema = read_put_body(request.json)

        # Instancia reposirtório
        item_repository = ItemRepository(session)

        # Edita item
        item_repository.update(schema)
        
        # Executa commit no banco de dados
        session.commit()

        # Retorno de sucesso da rota
        return get_default_success()
    except Exception as e:
        # Retorno de erro da rota
        return get_default_error(str(e))

def read_put_body(content) -> ItemEditSchema:
    id = int(request.json["id"])
    name = str(request.json["name"])
    type = str(request.json["type"])
    value = float(request.json["value"])

    return ItemEditSchema(id, name, type, value)