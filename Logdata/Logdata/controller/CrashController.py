from flask import request

from Logdata import DBManager
from Logdata.Log_Data_Blueprint import logdata


@logdata.route('/crash/<code>', methods=['PUT'])
def crash(code):
    if request.method == 'PUT':
        print(code)
        DBManager.crashDataInsert(request)
