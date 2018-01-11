import json
import pprint

from flask import render_template, request

from Logdata.Database import DBManager
from Logdata.Log_Data_Blueprint import logdata


@logdata.route('/')
def index():
    return render_template('index.html')


@logdata.route('/logdata', methods=['GET', 'POST'])
def logData():
    if request.method == 'GET':
        data = DBManager.getLogData()

        return render_template('logdata_view.html', logdata=data, tagFilter=logDataTagSelection())
    elif request.method == 'POST':
        jsonString = request.get_json()
        DBManager.logDataInsert(jsonString)
        return 'success'


@logdata.route('/logdatalevelfilter', methods=['POST'])
def logDataLevelFilter():
    print(request.form.get('logLevel'))
    if request.method == 'POST':
        data = DBManager.getLogDataLevelFilter(request.form.get('logLevel'))
        return render_template('logdata_view.html', logdata=data)


@logdata.route('/logdatatagfilter', methods=['POST'])
def logDataTagFilter():
    print(request.form.get('logTag'))
    if request.method == 'POST':
        data = DBManager.getLogDataTagFilter(request.form.get('logTag'))

        return render_template('logdata_view.html', logdata=data, tagFilter=logDataTagSelection())


def logDataTagSelection():
    projection = DBManager.getLogDataTagProjection()
    tagFilter = set()

    for item in projection:
        tagFilter.add(item['tag'])

    return tagFilter
