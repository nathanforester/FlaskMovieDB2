#!/bin/bash 

sudo apt update

sudo apt install python3-pip -y

pip install -r /home/ubuntu/FlaskMovieDB2/requirements.txt

python -m pip uninstall flask-sqlalchemy

python -m pip install flask-sqlalchemy

python3 /home/ubuntu/FlaskMovieDB2/create.py


