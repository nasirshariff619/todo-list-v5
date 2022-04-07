from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import uuid

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
app.config['SECRET_KEY'] = str(uuid.uuid4)
#export DATABASE_URI=mysql+pymysql://root:Database1324@10.46.128.3/flask-gcp-db

db = SQLAlchemy(app)

from application import routes