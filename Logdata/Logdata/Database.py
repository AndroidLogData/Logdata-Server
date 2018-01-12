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
                                             'nativePss': jsonString['nativePss'],
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
    def getLogData():
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

    @staticmethod
    def getLogDataLevelFilter(level):
        try:
            return mongo.db.logdata_android.find({'level': level})
        except Exception as e:
            print(e)
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def getLogDataTagFilter(tag):
        try:
            return mongo.db.logdata_android.find({'tag': tag})
        except Exception as e:
            print(e)
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def getLogDataTagProjection():
        try:
            return mongo.db.logdata_android.find({}, {'_id': False, 'tag': True})
        except Exception as e:
            print(e)
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def getLogDataMemoryProjection():
        try:
            return mongo.db.logdata_android.find_one({}, {'_id': False,
                                                          'totalMemory': True,
                                                          'availMemory': True,
                                                          'threshold': True,
                                                          'dalvikPss': True,
                                                          'nativePss': True,
                                                          'otherPss': True,
                                                          'totalPss': True})
        except Exception as e:
            print(e)
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)
