from flask import Flask,render_template,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect,Integer,Unicode,ForeignKey,Numeric
from sqlalchemy.orm import relationship
from flask_session import Session
from sqlalchemy_utils import create_database,database_exists
from sqlalchemy.ext.declarative import declarative_base

db=SQLAlchemy() #db by SQLAlchemy

from . import models #database models
from . import routes #blueprints
from . import utils
from . import currency



with open("allium.cfg") as config_file:
    for line in config_file:
        if line.find('TEMPLATE_NAME') != -1:
            template_name=line.split('"')[1::2][0]
app = Flask(__name__, static_folder='./templates/'+template_name+'/static/') #here flask is born

app.config.from_pyfile('../allium.cfg') #parse config into flask

currency_module=currency.FiatCurrency(app.config['CURRENCY']).module
#print(currency_module.exchange_rate)

#print (app.config['CURRENCY'])
#print(currency_module)

import random,string
secret_key=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(52))
app.secret_key=secret_key
app.config['SECRET_KEY']=secret_key
app.config['WTF_CSRF_SECRET_KEY']=secret_key

db.init_app(app) #db for app
#app.app_context().push()

#def reset_database():
#    db.drop_all()
#    db.create_all()
#    db.session.commit()
#checking for db and tables
with app.app_context():
    for table in models.all_tables:
        if not db.engine.has_table(table):
            db.create_all()
            models.populate.populate_tables(db)

app.register_blueprint(routes.base.base_blueprint)

app.register_blueprint(routes.admin.admin_blueprint) #registering blueprints for admin
app.register_blueprint(routes.admin_item.admin_item_blueprint) #registering blueprints for admin_item
app.register_blueprint(routes.admin_pictures.admin_picture_blueprint) #registering blueprints for admin_item

app.register_blueprint(routes.picture.picture_blueprint) #registering blueprints for admin_item
