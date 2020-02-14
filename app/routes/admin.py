from flask import Blueprint, render_template, session, request, make_response,abort
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from flask import current_app as app

admin_blueprint = Blueprint('admin', __name__)


# blueprint  for admin console
@admin_blueprint.route('/admin')
def admin():
    # todo rework adming,may be add session, but not necessary atm
    if request.cookies.get('masterkey') is not None:
        return render_template(app.config['TEMPLATE_NAME']+'/admin.html',config=app.config)
    else:
        # fixme add sessions for security
        class AdminForm(FlaskForm):
            master_key=PasswordField('Master key')
            submit = SubmitField('Log in')
        validation_form=AdminForm()

        response = make_response(redirect('/admin'))
        response.set_cookie('masterkey', '1')
        return response
@admin_blueprint.route('/admin_add')
def add_item():
    abort(400)