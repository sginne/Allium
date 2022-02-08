from flask import Response,Blueprint, render_template, session, request, make_response,abort,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField,PasswordField,TextField,HiddenField
from flask import current_app
import app
from .. import utils
from app import db,models,currency



class OrderForm(FlaskForm):
    address = TextAreaField('Address:')
    contact = TextAreaField('Contact:')

    submit = SubmitField('Submit')

order_blueprint = Blueprint('order', __name__) 
@order_blueprint.route('/order/<item_id>/<amount>/',methods=['GET','POST'])
def order(item_id,amount):
    try:
        item_id=str(int(item_id))
        amount=int(amount)
    except:
        item_id="0"
        amount=0
    finally:
        pass
    if request.method=='GET':
        order_form=OrderForm()
        item = db.session.query(models.Item).filter_by(id=item_id).all()
        item=utils.markup_list_descriptions(item)
        rate=app.currency_module.exchange_rate
        pictures = models.Picture.query.all()
        item = db.session.query(models.Item).filter_by(id=item_id).all()
        
        #private_key=app.currency_module.generate_private_key()
        #crypto_address=app.currency_module.address_from_key(private_key)
        #wif=app.currency_module.private_to_wif(private_key.hex())
        #print ("private key: ",private_key.hex())
        #print ("add: ",crypto_address)
		#print ("WIF: ",wif)
		


        return render_template(current_app.config['TEMPLATE_NAME']+'/order.html',form=order_form,amount=amount,rate=rate,fiat_name=app.currency_module.fiat_name,crypto_name=app.currency_module.crypto_name,items=item,pictures=pictures)
    elif request.method=='POST':
        
        try:
            item_id=str(int(item_id))
            amount=int(amount) #fixme why is it integer apriori?
        except:
            abort(404)
        finally:
            pass
        private_key=app.currency_module.generate_private_key()
        print (private_key)
		#new_order=models.Orders
	    #print (request.form['address'])
	    #print (request.form['contact'])
        return 'post'
