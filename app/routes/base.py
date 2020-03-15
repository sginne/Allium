from flask import Response,Blueprint, render_template, session, request, make_response,abort,redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField,PasswordField,TextField,HiddenField
#from flask import current_app as app
from flask import current_app
#from .. import currency
import app


from app import db,models,currency

base_blueprint = Blueprint('base', __name__) #registering admin blueprints

@base_blueprint.route('/',methods=['POST','GET'])
def base():

    #    print(app.currency_module.exchange_rate)
    return str(app.currency_module.exchange_rate)
