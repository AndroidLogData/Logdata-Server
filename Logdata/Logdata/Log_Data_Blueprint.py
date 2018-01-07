from flask import Blueprint

from Logdata.Log_Data_Logger import Log

logdata = Blueprint('flaskpractice', __name__, template_folder='../templates', static_folder='../static')

Log.info('static folder : %s' % logdata.static_folder)
Log.info('template folder : %s' % logdata.template_folder)
