from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

from . import models
from . import routes



app = Flask(__name__, static_folder='./static/')
app.config.from_pyfile('../allium.cfg')
db.init_app(app)
@app.route('/')
def hello_world():
    db.create_all()
    return render_template('base.html')