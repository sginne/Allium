from flask import Response,Blueprint, render_template, session, request, make_response,abort,redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField,PasswordField,TextField,HiddenField
from flask import current_app as app
from flask import current_app

from app import db,models


admin_blueprint = Blueprint('admin', __name__) #registering admin blueprints

@admin_blueprint.route('/admin',methods=['POST','GET'])
def admin():
    """
    route for admin dashboard
    """
    from .. import utils
    if request.cookies.get('masterkey') == utils.password_hashing(app.config['MASTER_PASSWORD']):
        #authorized
        orders = models.Orders.query.all()
        for order in orders:
            print(order)
        items=orders
        from .. import utils
        #items=utils.markup_list_descriptions(items)
        return render_template(app.config['TEMPLATE_NAME']+'/admin.html',config=app.config,active="admin-console",orders=orders)
    else:
        # fixme add sessions for security, maybe
        #not authorized, may by form posted
        class AdminForm(FlaskForm):
            master_key=PasswordField('Master password:')
            submit = SubmitField('Log in')
        validation_form=AdminForm()
        if request.method=='POST':
            #form posted?
            response = make_response(redirect('/admin'))
            #critical #fixme developer "any pass"
            #response.set_cookie('masterkey', utils.password_hashing(validation_form.master_key.data))
            response.set_cookie('masterkey', utils.password_hashing(app.config['MASTER_PASSWORD']))
            return response
        else:
            #return login form

            return render_template(app.config['TEMPLATE_NAME']+'/admin-login.html',form=validation_form)



@admin_blueprint.route('/reset')
def  reset():
    """
    Resetting database here, dangerous operation - #fixme
    """
    from . import utils
    if request.cookies.get('masterkey') == utils.password_hashing(app.config['MASTER_PASSWORD']):
        # authorized
        db.drop_all()
        db.create_all()
        db.session.commit()
    return redirect('/admin')
@admin_blueprint.route('/logout')
def logout():
    """
    route logout
    """
    response=make_response(redirect('/admin')) #fixme return to main
    response.set_cookie('masterkey','',0)
    return response
