from flask_openapi3 import OpenAPI, Info, Tag
from pydantic import BaseModel
from flask import redirect
from controllers import get_bill_items, post_bill_items, delete_bill_items, update_bill_items
from schemas import ExampleYearsListSchema, ExampleErrorSchema, ExampleSuccessSchema, ExamplePostSchema, ExamplePutSchema, ExampleDeleteSchema

# Inicializa API
info = Info(title="Financial Control API MVP 1", version="0.1.0")
app = OpenAPI(__name__, info=info)

# Documentação
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

# Rota GET
get_bill_items_tag = Tag(name="Buscar contas", description="Procuras as contas agrupadas por meses e anos.")
@app.get('/bill_items', tags=[get_bill_items_tag], responses={"200": ExampleYearsListSchema, "400": ExampleErrorSchema})
def get():
    return get_bill_items()

# Rota POST
post_bill_items_tag = Tag(name="Criar conta", description="Cria conta agrupada por mês e ano.")
@app.post('/bill_items', tags=[post_bill_items_tag], responses={"200": ExampleSuccessSchema, "400": ExampleErrorSchema})
def post(form: ExamplePostSchema):
    return post_bill_items(form)

# Rota PUT
put_bill_items_tag = Tag(name="Editar conta", description="Edita conta já criada.")
@app.put('/bill_items', tags=[put_bill_items_tag], responses={"200": ExampleSuccessSchema, "400": ExampleErrorSchema})
def put(form: ExamplePutSchema):
    return update_bill_items(form)

# Rota DELETE
delete_bill_items_tag = Tag(name="Deletar conta", description="Deleta conta já criada.")
@app.delete('/bill_items', tags=[delete_bill_items_tag], responses={"200": ExampleSuccessSchema, "400": ExampleErrorSchema})
def delete(form: ExampleDeleteSchema):
    return delete_bill_items(form)