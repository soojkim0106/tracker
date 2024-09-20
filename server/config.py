from flask import Flask
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_migrate import Migrate # type: ignore
from flask_restful import Api # type: ignore
from flask_cors import CORS # type: ignore
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)


CORS(app)