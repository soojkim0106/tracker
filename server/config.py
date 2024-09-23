from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

client_folder = os.path.join(os.getcwd(), "..", "client")
dist_folder = os.path.join(client_folder, "build")

db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)

app.config["SESSION_SQLALCHEMY"] = db

CORS(app)
