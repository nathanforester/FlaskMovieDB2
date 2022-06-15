#!/bin/bash 

sudo apt update
sudo apt-get install python3-venv -y
sudo apt install mysql-server -y

python3 -m venv venv
source venv/bin/activate
pip3 install -r /home/ubuntu/FlaskMovieDB2/requirements.txt

python3 /home/ubuntu/FlaskMovieDB2/create.py


