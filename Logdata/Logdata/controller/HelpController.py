from flask import render_template

from Logdata.Log_Data_Blueprint import logdata


@logdata.route('/help', methods=['GET'])
def help():
    return render_template('help.html')
