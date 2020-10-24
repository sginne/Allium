from flask import Response,Blueprint, render_template, session, request, make_response,abort,redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField,PasswordField,TextField,HiddenField
#from flask import current_app as app
from flask import current_app
#from .. import currency
import app
from .. import utils

from app import db,models,currency

base_blueprint = Blueprint('base', __name__) #registering admin blueprints

@base_blueprint.route('/',methods=['POST','GET'])

def base():

    item = db.session.query(models.Item).join(models.Fiat_currency).join(models.Crypto_currency).filter(
    models.Item.price_crypto_id == models.Crypto_currency.id).filter(
    models.Item.price_fiat_id == models.Fiat_currency.id).filter().all()
    item=utils.markup_list_descriptions(item)
    rate=app.currency_module.exchange_rate
    pictures = models.Picture.query.all()
    return render_template(current_app.config['TEMPLATE_NAME']+'/base.html',rate=rate,fiat_name=app.currency_module.fiat_name,crypto_name=app.currency_module.crypto_name,items=item,pictures=pictures)
