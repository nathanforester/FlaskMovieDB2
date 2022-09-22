from application import app
from flask import Flask
from jinja2.utils import markupsafe 


application = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
 
