from flask import Blueprint

from FlaskPractice.Log_Data_Logger import Log

flaskPractice = Blueprint('flaskpractice', __name__, template_folder='../templates', static_folder='../static')

Log.info('static folder : %s' % flaskPractice.static_folder)
Log.info('template folder : %s' % flaskPractice.template_folder)
