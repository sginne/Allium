from flask import Response,Blueprint, render_template, session, request, make_response,abort,redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField,PasswordField,TextField,HiddenField
from flask import current_app as app
from flask import current_app

from app import db,models


picture_blueprint = Blueprint('picture', __name__) #registering picture blueprints

@picture_blueprint.route('/picture',defaults={'pic_id':'0'})
@picture_blueprint.route('/picture/<pic_id>')

def picture(pic_id):

    try:
        abort(403)
    except:
        abort(404)
