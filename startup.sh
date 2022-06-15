#!/bin/bash 

sudo apt update
sudo apt-get install python3-venv -y

pip3 install -r /home/ubuntu/FlaskMovieDB2/requirements.txt

python3 /home/ubuntu/FlaskMovieDB2/create.py


