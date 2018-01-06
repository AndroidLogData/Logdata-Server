from flask import render_template
from flask_pymongo import PyMongo


class DBManager:
    @staticmethod
    def init(app):
        global mongo
        mongo = PyMongo(app)
        print("DBManager : " + str(app))

    @staticmethod
    def dataInsert(request):
        print(request.form)
        mongo.db.logdata_android.insert({'message': request.form['message'],
                                         'tag': request.form['tag'],
                                         'level': request.form['level']})
        data = mongo.db.logdata_android.find()
        # for d in data:
        #     print(d)
        return data
