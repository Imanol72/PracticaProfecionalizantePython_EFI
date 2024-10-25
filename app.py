import os #Versatil,completa y peligrosa ya que tiene todas las autorizaciones 

from datetime import timedelta
from flask import Flask, jsonify, render_template, request, url_for, redirect 

from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import(
    generate_password_hash,
    check_password_hash,
)
from flask_jwt_extended import (
    JWTManager,
)
from flask_cors import CORS
from flask_marshmallow import Marshmallow



app = Flask(__name__)

cors= CORS(app, resources={r"/*": {"origins": "*"}})
#Configuracion Alquemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
jwt = JWTManager(app)

from views import register_blueprints
register_blueprints(app)

load_dotenv()

#Serializador crea un objeto a un json