#!/bin/bash 

sudo apt update

sudo apt install python3-pip -y

pip install -r /home/ubuntu/FlaskMovieDB2/requirements.txt

python3 -m pip uninstall flask-sqlalchemy

python3 -m pip install flask-sqlalchemy

pip install flask

pip install flask_sqlalchemy

pip install sqlalchemy_utils

pip install pymysql

pip install flask_wtf

pip3 install python-dotenv

python3 /home/ubuntu/FlaskMovieDB2/create.py










