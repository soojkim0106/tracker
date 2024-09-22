from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_restful import Api 
from flask_cors import CORS 
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)


CORS(app)