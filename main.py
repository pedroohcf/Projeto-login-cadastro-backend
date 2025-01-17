from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__)
app.config.from_pyfile('config.py')

CORS(app)
db = SQLAlchemy(app)

from db import *

if __name__ == '__main__':
    app.run(debug=True)

