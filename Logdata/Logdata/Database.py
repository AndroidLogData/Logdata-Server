# -*- encoding=utf-8 -*-
import datetime

import pymongo
from flask import render_template
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
            mongo.db.logdata_android.insert({'packageName': jsonString['packageName'],
                                             'message': jsonString['message'],
                                             'tag': jsonString['tag'],
                                             'level': jsonString['level'],
                                             'time': datetime.datetime.strptime(jsonString['time'],
                                                                                '%Y-%m-%d %H:%M:%S'),
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
                                               'Time': datetime.datetime.strptime(jsonString['Time'],
                                                                                  '%Y-%m-%d %H:%M:%S')})
        except pymongo.errors.DuplicateKeyError as e:
            Log.error("중복되는 키가 존재합니다.: %s" % e)
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def getLogData():
        try:
            data = mongo.db.logdata_android.find().sort([('time', pymongo.DESCENDING)])
            if data.count() == 0:
                return None
            else:
                return data
        except Exception as e:
            print('getLogData' + str(e))
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def getCrashData():
        try:
            data = mongo.db.crashdata_android.find_one()
            if data.count() is None:
                return None
            else:
                return data
        except Exception as e:
            print('getCrashData' + str(e))
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def getLogDataLevelFilter(level):
        try:
            data = mongo.db.logdata_android.find({'level': level})
            if data.count() == 0:
                return None
            else:
                return data
        except Exception as e:
            print('getLogDataLevelFilter' + str(e))
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def getLogDataTagFilter(tag):
        try:
            data = mongo.db.logdata_android.find({'tag': tag})
            if data.count() == 0:
                return None
            else:
                return data
        except Exception as e:
            print('getLogDataTagFilter' + str(e))
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def getLogDataTagProjection():
        try:
            data = mongo.db.logdata_android.find({}, {'_id': False, 'tag': True})
            if data.count() == 0:
                return None
            else:
                return data
        except Exception as e:
            print('getLogDataTagProjection' + str(e))
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def getLogDataMemoryProjection():
        try:
            data = mongo.db.logdata_android.find_one({}, {'_id': False,
                                                          'totalMemory': True,
                                                          'availMemory': True,
                                                          'threshold': True,
                                                          'dalvikPss': True,
                                                          'nativePss': True,
                                                          'otherPss': True,
                                                          'totalPss': True})
            if not data:
                return None
            else:
                return data
        except Exception as e:
            print('getLogDataMemoryProjection' + str(e))
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def getCrashDataProjection(start='', end=''):
        try:
            if start == '' and end == '':
                data = mongo.db.crashdata_android.find_one({}, {'_id': False,
                                                                'Time': True})
                if not data:
                    return None
                else:
                    return data
            else:
                data = mongo.db.crashdata_android.find({'Time': {'$gt': start, '$lt': end}})
                if data.count() == 0:
                    return 'there is no data'
                else:
                    return data
        except Exception as e:
            print('getCrashDataProjection' + str(e))
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def getLogDataPackageNameProjection():
        try:
            data = mongo.db.logdata_android.find({}, {'_id': False,
                                                      'packageName': True})
            if data.count() == 0:
                return None
            else:
                return data
        except Exception as e:
            print('getLogDataMemoryProjection' + str(e))
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)

    @staticmethod
    def getLogDataPackageName(packageName):
        try:
            data = mongo.db.logdata_android.find({'packageName': packageName})
            if data.count() == 0:
                return None
            else:
                return data
        except Exception as e:
            print('getLogDataMemoryProjection' + str(e))
        except pymongo.errors.ServerSelectionTimeoutError as e:
            Log.error("서버 연결 실패 : %s" % e)
