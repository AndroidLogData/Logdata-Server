# -*- encoding=utf-8 -*-
import pymongo
from flask_pymongo import PyMongo
from pymongo import errors

from Logdata.Log_Data_Logger import Log
from Logdata.model.Logdata import Logdata


class DBManager:
    @staticmethod
    def init(app):
        try:
            global mongo
            mongo = PyMongo(app)
        except pymongo.errors.ConnectionFailure as e:
            Log.error("mongodb 연결 실패 : %s" % e)

    @staticmethod
    def logDataInsert(request):
        try:
            # mongo.db.logdata_android.insert({'message': request.form['message'],
            #                                  'tag': request.form['tag'],
            #                                  'level': request.form['level'],
            #                                  'time': request.form['time']})
            # mongo.db.logdata_android.insert(Logdata('hello', 'MainActivity', 'i', 1, 1, 1, 1, 1, True, 1, 1, 1))
            mongo.db.logdata_android.insert(Logdata(request.form['message'],
                                                    request.form['tag'],
                                                    request.form['level'],
                                                    request.form['time'],
                                                    request.form['totalMemory'],
                                                    request.form['availMemory'],
                                                    request.form['memoryPercentage'],
                                                    request.form['threshold'],
                                                    request.form['lowMemory'],
                                                    request.form['dalvikPss'],
                                                    request.form['otherPss'],
                                                    request.form['totalPss']))
        except pymongo.errors.DuplicateKeyError as e:
            Log.error("중복되는 키가 존재합니다.: %s" % e)
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def crashDataInsert(request):
        try:
            mongo.db.logdata_android.insert({'os': request.form['message']})
        except pymongo.errors.DuplicateKeyError as e:
            Log.error("중복되는 키가 존재합니다.: %s" % e)
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def getLogdata():
        try:
            return mongo.db.logdata_android.find().sort([('time', pymongo.ASCENDING)])
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)
