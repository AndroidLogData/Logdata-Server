from flask import Blueprint

flaskPractice = Blueprint('flaskpractice', __name__, template_folder='../templates', static_folder='../static')

print('static folder : %s' % flaskPractice.static_folder)
print('template folder : %s' % flaskPractice.template_folder)
