#!/bin/bash 

sudo apt update

sudo apt install python3-pip -y

pip install -r /home/ubuntu/FlaskMovieDB2/requirements.txt

python3 /home/ubuntu/FlaskMovieDB2/create.py


