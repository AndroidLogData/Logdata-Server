import datetime

from flask import render_template, request, jsonify

from Logdata.Log_Data_Blueprint import logdata
from Logdata.model.LogData import LogData


@logdata.route('/logdata', methods=['GET', 'POST'])
def logData():
    if request.method == 'GET':
        try:
            items = LogData.objects().all().order_by('-time')

            if items.count() == 0:
                return render_template('nodata.html')

            for item in items:
                item.totalMemory /= 1024 * 1024
                item.availMemory /= 1024 * 1024
                item.threshold /= 1024 * 1024
                item.dalvikPss /= 1024
                item.nativePss /= 1024
                item.otherPss /= 1024
                item.totalPss /= 1024

            # memoryLabels = ["totalMemory", "availMemory", "threshold"]
            # memoryColors = ["#F7464A", "#46BFBD", "#FDB45C"]
            #
            # pssLabels = ["dalvikPss", "nativePss", "otherPss", "totalPss"]
            # pssColors = ["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA"]
            #
            # labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
            # values = [10, 9, 8, 7, 6, 4, 7, 8]
            # colors = ["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA", "#ABCDEF", "#DDDDDD", "#ABCABC"]

            return render_template('logdata_view.html',
                                   logdata=items,
                                   tagFilter=logDataTagSelection(),
                                   packageNameFilter=logDataPackageNameSelection())
        except Exception as e:
            print(e)
    elif request.method == 'POST':
        jsonString = request.get_json()
        data = LogData(jsonString['packageName'],
                       jsonString['message'],
                       jsonString['tag'],
                       jsonString['level'],
                       datetime.datetime.strptime(jsonString['time'], '%Y-%m-%d %H:%M:%S'),
                       jsonString['totalMemory'],
                       jsonString['availMemory'],
                       jsonString['memoryPercentage'],
                       jsonString['threshold'],
                       jsonString['lowMemory'],
                       jsonString['dalvikPss'],
                       jsonString['nativePss'],
                       jsonString['otherPss'],
                       jsonString['totalPss'])
        data.save()
        return jsonify({'result': 'success'})


@logdata.route('/logdatalevelfilter/<string:level>', methods=['GET'])
def logDataLevelFilter(level):
    if request.method == 'GET':
        items = LogData.objects(level=level).all()

        if items.count() == 0:
            return render_template('nodata.html')

        return render_template('logdata_view.html', logdata=items, tagFilter=logDataTagSelection())


@logdata.route('/logdatatagfilter/<string:tag>', methods=['GET'])
def logDataTagFilter(tag):
    if request.method == 'GET':
        items = LogData.objects(tag=tag)

        if items.count() == 0:
            return render_template('nodata.html')

        return render_template('logdata_view.html', logdata=items, tagFilter=logDataTagSelection())


def logDataTagSelection():
    projection = LogData.objects().all()
    tagFilter = set()

    for item in projection:
        tagFilter.add(item.tag)

    return tagFilter


def logDataPackageNameSelection():
    projection = LogData.objects().all()
    packageNameFilter = set()

    for item in projection:
        packageNameFilter.add(item.packageName)

    return packageNameFilter


@logdata.route('/logdatapackagename/<string:packageName>', methods=['GET'])
def logDataPackageName(packageName):
    if request.method == 'GET':
        items = LogData.objects(packageName=packageName).all().order_by('-time')

        if items.count() == 0:
            return render_template('nodata.html')

        return render_template('logdata_view.html',
                               logdata=items,
                               tagFilter=logDataTagSelection(),
                               packageNameFilter=logDataPackageNameSelection())
