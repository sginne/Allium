from flask import send_file,Response,Blueprint, render_template, session, request, make_response,abort,redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField,PasswordField,TextField,HiddenField
from flask import current_app as app
from flask import current_app
import os,io

from app import db,models


picture_blueprint = Blueprint('picture', __name__) #registering picture blueprints

@picture_blueprint.route('/picture',defaults={'pic_id':'0'})
@picture_blueprint.route('/picture/<pic_id>')

def picture(pic_id):
    template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    template_dir=template_dir+"/images/"
    print(template_dir)
    with open(template_dir+"0.jpg", 'rb') as bites:
        return send_file(
                     io.BytesIO(bites.read()),
                     attachment_filename='logo.jpeg',
                     mimetype='image/jpg'
               )