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
    #print(pic_id)
    if not(pic_id=="0") or (pic_id==""):
        pictures=models.Picture.query.all()
        for picture in pictures:
            import base64
            if pic_id==picture.name:
                #print(picture.name)
                #b64_string = picture.picture+"=" * ((4 - len(picture.picture) % 4) % 4)#padding?
                import re
                b64_string=re.sub('^data:image/.+;base64,', '',picture.picture)
                image_binary=base64.b64decode(b64_string)
                #print(image_binary)
                from PIL import Image
                image=Image.open(io.BytesIO(image_binary))

                return send_file(io.BytesIO(image_binary),attachment_filename=picture.name+".jpg",mimetype="image/jpg",as_attachment=False)

    template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    template_dir=template_dir+"/images/"
    with open(template_dir+"0.jpg", 'rb') as bites:
        return send_file(io.BytesIO(bites.read()),attachment_filename='0.jpeg',mimetype='image/jpg')