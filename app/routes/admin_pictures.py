from flask import Response,Blueprint, render_template, session, request, make_response,abort,redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField,PasswordField,TextField,HiddenField
from flask import current_app as app
from flask import current_app
from app import db,models
from .. import utils
admin_picture_blueprint = Blueprint('admin_pictures', __name__)

@admin_picture_blueprint.route('/admin_add_picture',methods=['POST','GET'])
def add_picture():
    """
    route for adding picture
    """
    from .. import utils
    if request.cookies.get('masterkey') == utils.password_hashing(app.config['MASTER_PASSWORD']):
        class AddPictureForm(FlaskForm):
            name=StringField('Item name:')
            picture=HiddenField('Picture')
            submit = SubmitField('Add')
        add_picture_form=AddPictureForm()
        if request.method == 'POST':
            new_item=models.Picture(name=add_picture_form.name.data,picture=add_picture_form.picture.data)
            db.session.add(new_item)
            db.session.commit()
            return redirect('/admin_modify_picture')

        return render_template(app.config['TEMPLATE_NAME'] + '/admin-add-picture.html', config=app.config, active="add-picture",form=add_picture_form)

    else:
        return redirect('/admin')

@admin_picture_blueprint.route('/admin_modify_picture')
def modify_picture():
    """
    route to modify picture
    """
    from .. import utils
    if request.cookies.get('masterkey') == utils.password_hashing(app.config['MASTER_PASSWORD']):
        pictures=models.Picture.query.all()
        return render_template(app.config['TEMPLATE_NAME'] + '/admin-modify-picture.html', config=app.config, active="modify-picture",pictures=pictures)
    else:
        return redirect('/admin')


