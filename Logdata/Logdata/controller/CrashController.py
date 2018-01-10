from flask import request

from Logdata.Log_Data_Blueprint import logdata


@logdata.route('/crash', methods=['POST'])
def crash():
    if request.method == 'POST':
        print(request.get_json())
        return 'success'
