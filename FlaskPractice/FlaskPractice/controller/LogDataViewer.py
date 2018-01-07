from flask import render_template, request
from FlaskPractice.FlackPractice_blueprint import flaskPractice
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
        data = DBManager.dataInsert(request)
        # return 'PUT'
        # print("adsfjore : " + str(mongo))
        # mongo.db.logdata_android.insert({'message': request.form['message'],
        #                                  'tag': request.form['tag'],
        #                                  'level': request.form['level']})
        # data = mongo.db.logdata_android.find()
        for d in data:
            print(d)
        return 'success'
