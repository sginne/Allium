from flask import Blueprint, render_template, session, request, make_response
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from flask import current_app as app

admin_blueprint = Blueprint('admin', __name__)


# blueprint  for admin console
@admin_blueprint.route('/admin')
def admin():
    data_to_template=[]
    # todo rework adming,may be add session, but not necessary
    if request.cookies.get('masterkey') is not None:
        config_to_template=app.config
        return render_template('admin.html',config=app.config)
    else:
        # fixme add sessions for security
        class AdminForm(FlaskForm):
            master_key=PasswordField('Master key')
            submit = SubmitField('Log in')
        validation_form=AdminForm()

        response = make_response(redirect('/admin'))
        response.set_cookie('masterkey', '1')
        return response
