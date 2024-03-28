from flask import Flask
from routes import api

# Inicializa API
app = Flask(__name__)

# Inicializa rotas
app.register_blueprint(api)
