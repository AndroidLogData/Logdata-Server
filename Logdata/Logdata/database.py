import pymongo
from flask_pymongo import PyMongo


class DBManager:
    @staticmethod
    def init(app):
        global mongo
        mongo = PyMongo(app)

    @staticmethod
    def dataInsert(request):
        print(request.form)
        mongo.db.logdata_android.insert({'message': request.form['message'],
                                         'tag': request.form['tag'],
                                         'level': request.form['level'],
                                         'time': request.form['time']})

    @staticmethod
    def getLogdata():
        return mongo.db.logdata_android.find().sort([('time', pymongo.ASCENDING)])
