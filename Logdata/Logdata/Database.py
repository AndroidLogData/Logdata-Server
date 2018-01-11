# -*- encoding=utf-8 -*-
import pymongo
from flask_pymongo import PyMongo
from Logdata.Log_Data_Logger import Log
from pymongo import errors


class DBManager:
    @staticmethod
    def init(app):
        try:
            global mongo
            mongo = PyMongo(app)
        except pymongo.errors.ConnectionFailure as e:
            Log.error("mongodb 연결 실패 : %s" % e)

    @staticmethod
    def logDataInsert(jsonString):
        try:
            mongo.db.logdata_android.insert({'message': jsonString['message'],
                                             'tag': jsonString['tag'],
                                             'level': jsonString['level'],
                                             'time': jsonString['time'],
                                             'totalMemory': jsonString['totalMemory'],
                                             'availMemory': jsonString['availMemory'],
                                             'memoryPercentage': jsonString['memoryPercentage'],
                                             'threshold': jsonString['threshold'],
                                             'lowMemory': jsonString['lowMemory'],
                                             'dalvikPss': jsonString['dalvikPss'],
                                             'otherPss': jsonString['otherPss'],
                                             'totalPss': jsonString['totalPss']})
        except Exception as e:
            print(e)
        except pymongo.errors.DuplicateKeyError as e:
            Log.error("중복되는 키가 존재합니다.: %s" % e)
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def crashDataInsert(jsonString):
        try:
            mongo.db.crashdata_android.insert({'AndroidVersion': jsonString['AndroidVersion'],
                                               'APPVersionCode': jsonString['APPVersionCode'],
                                               'APPVersionName': jsonString['APPVersionName'],
                                               'AvailableMemorySize': jsonString['AvailableMemorySize'],
                                               'Brand': jsonString['Brand'],
                                               'Build': jsonString['Build'],
                                               'DeviceID': jsonString['DeviceID'],
                                               'Display': jsonString['Display'],
                                               'DeviceFeatures': jsonString['DeviceFeatures'],
                                               'Environment': jsonString['Environment'],
                                               'Logcat': jsonString['Logcat'],
                                               'Time': jsonString['Time']})
        except pymongo.errors.DuplicateKeyError as e:
            Log.error("중복되는 키가 존재합니다.: %s" % e)
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def getLogdata():
        try:
            return mongo.db.logdata_android.find().sort([('time', pymongo.DESCENDING)])
        except Exception as e:
            print(e)
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def getCrashData():
        try:
            return mongo.db.crashdata_android.find_one()
            # return mongo.db.crashdata_android.find_one().sort([('time', pymongo.DESCENDING)])
        except Exception as e:
            print(e)
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)
