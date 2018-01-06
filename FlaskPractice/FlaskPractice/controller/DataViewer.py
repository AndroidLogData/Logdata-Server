from flask import render_template, request
from FlaskPractice.FlackPractice_blueprint import flaskPractice
from FlaskPractice.database import DBManager


@flaskPractice.route('/logdata', methods=['PUT'])
def logData():
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
        return render_template('logdata_view.html', data=data)
