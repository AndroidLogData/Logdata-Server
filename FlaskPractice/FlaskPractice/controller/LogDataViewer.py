from flask import render_template, request
from FlaskPractice.Log_Data_Blueprint import flaskPractice
from FlaskPractice.database import DBManager


@flaskPractice.route('/')
def index():
    return render_template('index.html')


@flaskPractice.route('/logdata', methods=['GET', 'PUT'])
def logData():
    if request.method == 'GET':
        data = DBManager.getLogdata()
        return render_template('logdata_view.html', logdata=data)
    if request.method == 'PUT':
        DBManager.dataInsert(request)
        return 'success'
