from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()
from . import models


app = Flask(__name__, static_folder='./static/',)
db.init_app(app)
app.config.from_pyfile('allium.cfg')
@app.route('/')
def hello_world():
    db.create_all()
    return render_template('base.html')