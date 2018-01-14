from flask import render_template
from Logdata import DBManager
from Logdata.Log_Data_Blueprint import logdata


@logdata.route('/')
def index():
    data = DBManager.getLogDataPackageNameProjection()
    values = set()

    for d in data:
        values.add(d['packageName'])

    print(values)
    return render_template('main.html', values=values)
