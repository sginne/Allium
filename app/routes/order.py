from flask import Response,Blueprint, render_template, session, request, make_response,abort,redirect

from wtforms import TextAreaField,StringField,SubmitField,PasswordField,TextField,HiddenField
#from flask import current_app as app
from flask import current_app
#from .. import currency
import app
from .. import utils

from app import db,models,currency

order_blueprint = Blueprint('order', __name__) #registering admin blueprints

@order_blueprint.route('/order/<item_id>/<amount>/',methods=['GET'])
def order(item_id,amount):
	return item_id+' '+amount

