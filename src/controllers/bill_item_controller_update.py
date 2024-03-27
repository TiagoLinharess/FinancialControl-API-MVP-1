from flask import Blueprint, request
from repositories.item import ItemRepository
from models import Session
from schemas.edit import ItemEditSchema

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
        return { "sussess": True }, 200
    except Exception as e:
        # Retorno de erro da rota
        return { "error": str(e) }, 400

def read_put_body(content) -> ItemEditSchema:
    id = int(request.json["id"])
    name = str(request.json["name"])
    type = str(request.json["type"])
    value = float(request.json["value"])

    return ItemEditSchema(id, name, type, value)