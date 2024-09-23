from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_restful import Api 
from flask_cors import CORS 
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)


CORS(app)
