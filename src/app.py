from flask_openapi3 import OpenAPI, Info, Tag
from pydantic import BaseModel
from flask import redirect
from routes import api
from schemas import ExampleYearsListSchema, ExampleErrorSchema, ExampleSuccessSchema, ExamplePostSchema, ExamplePutSchema, ExampleDeleteSchema

# Inicializa API
info = Info(title="Financial Control API MVP 1", version="0.1.0")
app = OpenAPI(__name__, info=info)

# Inicializa rotas
app.register_blueprint(api)

# Documentação
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

get_bill_items_tag = Tag(name="Buscar contas", description="Procuras as contas agrupadas por meses e anos.")
@app.get('/bill_items', tags=[get_bill_items_tag], responses={"200": ExampleYearsListSchema, "400": ExampleErrorSchema})
def example_get():
    return

post_bill_items_tag = Tag(name="Criar conta", description="Cria conta agrupada por mês e ano.")
@app.post('/bill_items', tags=[post_bill_items_tag], responses={"200": ExampleSuccessSchema, "400": ExampleErrorSchema})
def example_post(form: ExamplePostSchema):
    return

put_bill_items_tag = Tag(name="Editar conta", description="Edita conta já criada.")
@app.put('/bill_items', tags=[put_bill_items_tag], responses={"200": ExampleSuccessSchema, "400": ExampleErrorSchema})
def example_put(form: ExamplePutSchema):
    return

delete_bill_items_tag = Tag(name="Deletar conta", description="Deleta conta já criada.")
@app.delete('/bill_items', tags=[delete_bill_items_tag], responses={"200": ExampleSuccessSchema, "400": ExampleErrorSchema})
def example_delete(form: ExampleDeleteSchema):
    return