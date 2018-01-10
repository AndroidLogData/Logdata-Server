from flask import request

from Logdata import DBManager
from Logdata.Log_Data_Blueprint import logdata


@logdata.route('/crash', methods=['POST'])
def crash():
    if request.method == 'POST':
        jsonString = request.get_json()
        print(jsonString)
        DBManager.crashDataInsert(jsonString)
        return 'success'
