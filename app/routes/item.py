from flask import Response,Blueprint, render_template, session, request, make_response,abort,redirect

from wtforms import TextAreaField,StringField,SubmitField,PasswordField,TextField,HiddenField
#from flask import current_app as app
from flask import current_app
#from .. import currency
import app
from .. import utils

from app import db,models,currency

item_blueprint = Blueprint('item', __name__) #registering admin blueprints

@item_blueprint.route('/item/<item_id>/',methods=['GET'])
def item(item_id):
	try:
		item_id=str(int(item_id))
	except:
		item_id="0"
	finally:
		pass
	item = db.session.query(models.Item).filter_by(id=item_id).all()
	rate=app.currency_module.exchange_rate
	pictures = models.Picture.query.all()

	print(item)
	return render_template(current_app.config['TEMPLATE_NAME']+'/item.html',rate=rate,fiat_name=app.currency_module.fiat_name,crypto_name=app.currency_module.crypto_name,items=item,pictures=pictures)
