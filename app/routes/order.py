from flask import Response,Blueprint, render_template, session, request, make_response,abort,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField,PasswordField,TextField,HiddenField
from flask import current_app
import app
from .. import utils
from app import db,models,currency
from datetime import datetime



class OrderForm(FlaskForm):
    address = TextAreaField('Address:')
    contact = TextAreaField('Contact:')

    submit = SubmitField('Submit')

order_blueprint = Blueprint('order', __name__) 
@order_blueprint.route('/order/w/',methods=['GET']) #fixme test route
def plug():
    return "test"
@order_blueprint.route('/order/w/<wallet>/',methods=['GET'])
def done_order(wallet):
        
        #print ("here")
        #print(app.currency_module.read_wallet(wallet))
        rate=app.currency_module.exchange_rate
        try:
        #for i in range(0,1):
            wallet=str(wallet)
            #app.currency_module.read_wallet_current_state(wallet)
            #print("Final balance",app.currency_module.read_wallet_final_balance(wallet))
            orders = db.session.query(models.Orders).filter_by(public_wallet=wallet).all()
            #print(orders[0])
            order_wallet=orders[0].public_wallet
            order_name=orders[0].ordered_name
            order_price=orders[0].price_crypto
            order_status=orders[0].status
        #try:
        #    pass
        except:
            abort(404)
        finally:pass
        payment_link=app.currency_module.link(order_wallet,order_price,order_name,"Payment link")

        
        return render_template(current_app.config['TEMPLATE_NAME']+'/payment.html',rate=rate,fiat_name=app.currency_module.fiat_name,crypto_name=app.currency_module.crypto_name,wallet=order_wallet,name=order_name,price=order_price,link=payment_link,status=order_status)
        
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
        if request.form['contact']=='' or request.form['address']=='': return 'Please fill in information'
        rate=app.currency_module.exchange_rate
        try:
            item_id=str(int(item_id))
            amount=int(amount) 
        except:
            abort(404)
        finally:
            pass
        private_key=app.currency_module.generate_private_key()
        public_wallet=app.currency_module.address_from_key(private_key)
        item = db.session.query(models.Item).filter_by(id=item_id).all()
        try:
            ordered_name="({})x{}".format(item[0].name,amount)

            if (item[0].fiat_crypto_main_flag=='crypto'):
                order_price=float(item[0].price_crypto)*amount
            else:
                order_price=float(item[0].price_fiat*amount)/rate
        except:
            pass
        finally:
            pass
        current_datetime=datetime.now()
        #ordered_name="({])x{}".format(item[0].name,item[0].amount)
        new_order=models.Orders(public_wallet=public_wallet,private_key=private_key.hex(),price_crypto=order_price,ordered_name=ordered_name,address=str(request.form['address']),contact_info=str(request.form['contact']),date=int(round(current_datetime.timestamp())))
        db.session.add(new_order)
        db.session.commit()
        #print (request.form['address'])
	    #print (request.form['contact'])
        return redirect("/order/w/{}".format(public_wallet))
