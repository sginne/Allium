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
	try:
		item_id=str(int(item_id))
		amount=int(amount)
	except:
		item_id="0"
	finally:
		pass
	item = db.session.query(models.Item).filter_by(id=item_id).all()
	item=utils.markup_list_descriptions(item)
	rate=app.currency_module.exchange_rate
	pictures = models.Picture.query.all()
	item = db.session.query(models.Item).filter_by(id=item_id).all()


	return render_template(current_app.config['TEMPLATE_NAME']+'/order.html',amount=amount,rate=rate,fiat_name=app.currency_module.fiat_name,crypto_name=app.currency_module.crypto_name,items=item,pictures=pictures)
