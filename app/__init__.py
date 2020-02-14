from flask import Flask,render_template,session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session


db=SQLAlchemy() #db by SQLAlchemy


from . import models #database models
from . import routes #blueprints



app = Flask(__name__, static_folder='./static/') #here flask is born

app.config.from_pyfile('../allium.cfg') #parse config into flask

db.init_app(app) #db for app
Session(app) #Session

app.register_blueprint(routes.admin.admin_blueprint) #registering blueprints for admin
