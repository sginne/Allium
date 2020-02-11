from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()
from . import models


app = Flask(__name__, static_folder='./static/',)
app.config.from_pyfile('allium.cfg')
@app.route('/')
def hello_world():
    return render_template('base.html')