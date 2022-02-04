from flask import Response,Blueprint, render_template, session, request, make_response,abort,redirect
from flask_wtf import FlaskForm
from wtforms import RadioField,FloatField,TextAreaField,StringField,SubmitField,PasswordField,TextField,HiddenField
from flask import current_app as app
from flask import current_app
from app import db,models
from .. import utils

admin_item_blueprint = Blueprint('admin_item', __name__)
class ItemForm(FlaskForm):
    name = StringField('Item name:')
    description = TextAreaField('Description:')
    price_crypto=FloatField('Crypto price')
    price_fiat=FloatField('FIAT price')
    pic_name=StringField('Head picture:')
    amount=StringField('Amount(-1=∞)')
    amount_palette=StringField('1,2,3,4,5 - sell amount presets')
    currency=RadioField('FIAT/Crypto main flag',choices=[(1, 'fiat'), (2, 'crypto')],default=1)
    short_description=StringField('Small description')
    submit = SubmitField('')


@admin_item_blueprint.route('/admin_add',methods=['POST','GET'])
def add_item():
    """
    route for adding item to database
    """
    if request.cookies.get('masterkey') == utils.password_hashing(app.config['MASTER_PASSWORD']):
        # authorized
        add_form=ItemForm()
        if request.method=='POST':
            #adding item?
            if add_form.currency.data=='2':
                fiat_crypto_main_flag="crypto"
            else:
                fiat_crypto_main_flag="fiat"
            new_item=models.Item(name=add_form.name.data,description=add_form.description.data,pic_name=add_form.pic_name.data,price_crypto=add_form.price_crypto.data,price_fiat=add_form.price_fiat.data,price_crypto_id=1,price_fiat_id=1,fiat_crypto_main_flag=fiat_crypto_main_flag)#fixme ..=1 is lame way to reference crypto and fiat id
            db.session.add(new_item)
            db.session.commit()
            return redirect('/admin_modify')
        else:
            return render_template(app.config['TEMPLATE_NAME'] + '/admin-add.html', config=app.config,active="add-good",form=add_form,items=[''])#fixme enchance default perhaps
    else:
        return redirect('/admin')

@admin_item_blueprint.route('/admin_modify/<action>/<post_id>',methods=['POST','GET'])
@admin_item_blueprint.route('/admin_modify',methods=['GET'])
def modify_item(action='default',post_id=None):
    """
    route for item modification
    :return:
    """

    if request.cookies.get('masterkey') == utils.password_hashing(app.config['MASTER_PASSWORD']):
        # authorized

        if action=='modify':
            #post_id to modify
            item=db.session.query(models.Item).join(models.Fiat_currency).join(models.Crypto_currency).filter(models.Item.price_crypto_id==models.Crypto_currency.id).filter(models.Item.price_fiat_id==models.Fiat_currency.id).filter(models.Item.id==post_id).all()
            modify_form=ItemForm()
            if request.method=='POST':
                item[0].name=modify_form.name.data
                item[0].description=modify_form.description.data
                item[0].price_crypto=modify_form.price_crypto.data
                item[0].price_fiat=modify_form.price_fiat.data
                item[0].amount=modify_form.amount.data
                item[0].amount_palette=modify_form.amount_palette.data
                item[0].pic_name=modify_form.pic_name.data
                item[0].short_description=modify_form.short_description.data
                if modify_form.currency.data=='1':
                    item[0].fiat_crypto_main_flag='fiat'
                else:
                    item[0].fiat_crypto_main_flag='crypto'
                db.session.commit()
                return redirect('/admin_modify')
            return render_template(app.config['TEMPLATE_NAME']+'/admin-modify-item.html',config=app.config,active="modify-good",items=item,form=modify_form)
        elif action=='delete':
            models.Item.query.filter_by(id=post_id).delete()
            db.session.commit()
            return redirect('/admin_modify')
        else:
            items = db.session.query(models.Item).join(models.Fiat_currency).join(models.Crypto_currency).filter(models.Item.price_crypto_id==models.Crypto_currency.id).filter(models.Item.price_fiat_id==models.Fiat_currency.id).all()
            items=utils.markup_list_descriptions(items)
            return render_template(app.config['TEMPLATE_NAME'] + '/admin-modify.html', config=app.config, active="modify-good",items=items)
    else:
        return redirect('/admin')
