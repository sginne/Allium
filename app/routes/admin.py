from flask import Blueprint, render_template
s="s"
admin_blueprint=Blueprint('admin',__name__)
@admin_blueprint.route('/admin')
def hello_world():
    return render_template('admin.html')