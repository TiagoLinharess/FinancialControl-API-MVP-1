from repositories import ItemRepository
from models import Session
from schemas import ItemEditSchema, get_default_error, get_default_success, ExamplePutSchema

# Rota de UPDATE do endpoint de Bill Items
def update_bill_items(form: ExamplePutSchema):
    try:
        # Cria sessão
        session = Session()

        # Procura campo id no body
        schema = read_put_body(form)

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

def read_put_body(form: ExamplePutSchema) -> ItemEditSchema:
    id = int(form.id)
    name = form.name
    type = form.type
    value = float(form.value)

    return ItemEditSchema(id, name, type, value)