import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

app = Flask(__name__)
db = SQLAlchemy(app)

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
environ  = os.environ.get('DB_ENDPOINT')
name     = os.environ.get('DB_NAME')

url = f'mysql+pymysql://{username}:{password}@{environ}/{name}'
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SECRET_KEY'] = '123456789'

db = SQLAlchemy(app)

engine= create_engine(url, echo=True)
if not database_exists(engine.url):
    create_database(engine.url)
else:
    engine.connect()

import application.routes 