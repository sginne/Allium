from flask import Blueprint, render_template, session, request, make_response,abort,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from flask import current_app as app
import hashlib

def password_hashing(password):
    """
    Returns sha512 from password and app.config['SECRET_KEY']
    :param password: password string
    :return: salted and hashed password
    """
    return hashlib.pbkdf2_hmac('sha512',password.encode('utf-8'),app.config['SECRET_KEY'].encode('utf-8'),66766).hex()#fix me 66766 is for no reason

admin_blueprint = Blueprint('admin', __name__) #registering admin blueprints

@admin_blueprint.route('/admin',methods=['POST','GET'])
def admin():
    """
    route for admin dashboard
    """
    if request.cookies.get('masterkey') == password_hashing(app.config['MASTER_PASSWORD']):
        return render_template(app.config['TEMPLATE_NAME']+'/admin.html',config=app.config)
    else:
        # fixme add sessions for security, maybe
        class AdminForm(FlaskForm):
            master_key=PasswordField('Master password:')
            submit = SubmitField('Log in')
        validation_form=AdminForm()
        if request.method=='POST':
            response = make_response(redirect('/admin'))
            response.set_cookie('masterkey', password_hashing(validation_form.master_key.data))
            return response
        else:
            return render_template(app.config['TEMPLATE_NAME']+'/admin-login.html',form=validation_form)


@admin_blueprint.route('/admin_add')
def add_item():
    """
    route for adding item to database
    """
    abort(400)

@admin_blueprint.route('/logout')
def logout():
    """
    route logout
    """
    response=make_response(redirect('/admin')) #fixme return to main
    response.set_cookie('masterkey','',0)
    return response