from flask import Response,Blueprint, render_template, session, request, make_response,abort,redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField,PasswordField,TextField
from flask import current_app as app
from flask import current_app
import hashlib
from app import db,models

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
        #authorized
        items = models.Item.query.all()
        return render_template(app.config['TEMPLATE_NAME']+'/admin.html',config=app.config,active="admin-console",items=items)
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
            response.set_cookie('masterkey', password_hashing(validation_form.master_key.data))
            return response
        else:
            #return login form

            return render_template(app.config['TEMPLATE_NAME']+'/admin-login.html',form=validation_form)


@admin_blueprint.route('/admin_add',methods=['POST','GET'])
def add_item():
    """
    route for adding item to database
    """
    if request.cookies.get('masterkey') == password_hashing(app.config['MASTER_PASSWORD']):
        # authorized
        class AddForm(FlaskForm):
            name=StringField('Item name:')
            description=TextAreaField('Description:')
            submit = SubmitField('Add')
        add_form=AddForm()
        if request.method=='POST':
            #adding item?
            new_item=models.Item(name=add_form.name.data,description=add_form.description.data)

            db.session.add(new_item)
            db.session.commit()
            return redirect('/admin')
        else:
            return render_template(app.config['TEMPLATE_NAME'] + '/admin-add.html', config=app.config,active="add-good",form=add_form)
    else:
        return redirect('/admin')
@admin_blueprint.route('/reset')
def  reset():
    if request.cookies.get('masterkey') == password_hashing(app.config['MASTER_PASSWORD']):
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