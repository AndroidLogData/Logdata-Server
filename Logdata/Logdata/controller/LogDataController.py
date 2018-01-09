from flask import render_template, request
from Logdata.Log_Data_Blueprint import logdata
from Logdata.Database import DBManager


@logdata.route('/')
def index():
    return render_template('index.html')


@logdata.route('/logdata', methods=['GET', 'PUT'])
def logData():
    if request.method == 'GET':
        data = DBManager.getLogdata()
        return render_template('logdata_view.html', logdata=data)
    if request.method == 'PUT':
        DBManager.logDataInsert(request)
        return 'success'
