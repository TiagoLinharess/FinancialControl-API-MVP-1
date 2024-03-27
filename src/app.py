from flask import Flask, jsonify, request
from models import Session, Year
from routes import api

# Inicializa API
app = Flask(__name__)

# Inicializa rotas
app.register_blueprint(api)
