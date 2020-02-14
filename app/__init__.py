from flask import Flask,render_template,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect,Integer
from sqlalchemy.orm import relationship
from flask_session import Session
from sqlalchemy_imageattach.entity import Image,image_attachment
from sqlalchemy_utils import create_database,database_exists

db=SQLAlchemy() #db by SQLAlchemy

from . import models #database models
from . import routes #blueprints



app = Flask(__name__, static_folder='./static/') #here flask is born

app.config.from_pyfile('../allium.cfg') #parse config into flask

db.init_app(app) #db for app

#checking for db and tables
with app.app_context():
    for table in models.all_tables:
        if not db.engine.has_table(table):
            db.create_all()
            db.session.commit()
            pass


app.register_blueprint(routes.admin.admin_blueprint) #registering blueprints for admin
