import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
from pathlib import Path

app = Flask(__name__)
db = SQLAlchemy(app)

username = Path('/home/ubuntu/username')
password = Path('/home/ubuntu/password')
endpoint  = Path('/home/ubuntu/endpoint')
name     = Path('/home/ubuntu/name')
load_dotenv(stream=f'{username}:{password}@{endpoint}/{name}')

url = f'mysql+pymysql://{load_dotenv}'
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SECRET_KEY'] = '123456789'

db = SQLAlchemy(app)

engine= create_engine(url, echo=True)
if not database_exists(engine.url):
    create_database(engine.url)
else:
    engine.connect()

import application.routes 