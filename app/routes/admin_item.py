from flask import Response,Blueprint, render_template, session, request, make_response,abort,redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField,PasswordField,TextField,HiddenField
from flask import current_app as app
from flask import current_app
from app import db,models
from .. import utils
admin_item_blueprint = Blueprint('admin_item', __name__)



@admin_item_blueprint.route('/admin_add',methods=['POST','GET'])
def add_item():
    """
    route for adding item to database
    """
    if request.cookies.get('masterkey') == utils.password_hashing(app.config['MASTER_PASSWORD']):
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
