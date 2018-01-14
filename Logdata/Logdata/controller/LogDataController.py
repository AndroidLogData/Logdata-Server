from flask import render_template, request
from Logdata.Database import DBManager
from Logdata.Log_Data_Blueprint import logdata


@logdata.route('/logdata', methods=['GET', 'POST'])
@logdata.route('/logdata/<string:level>', methods=['GET'])
def logData(level=''):
    if request.method == 'GET':
        if level in ['i', 'v', 'e', 'w', 'd']:
            data = DBManager.getLogDataLevelFilter(level)

            if data is None:
                return render_template('nodata.html')
            else:
                return render_template('logdata_view.html', logdata=data, tagFilter=logDataTagSelection())
        else:
            data = DBManager.getLogData()
            memory = DBManager.getLogDataMemoryProjection()

            if data is None or memory is None:
                return render_template('nodata.html')

            memory['totalMemory'] /= 1024 * 1024
            memory['availMemory'] /= 1024 * 1024
            memory['threshold'] /= 1024 * 1024
            memory['dalvikPss'] /= 1024
            memory['nativePss'] /= 1024
            memory['otherPss'] /= 1024
            memory['totalPss'] /= 1024

            memoryLabels = ["totalMemory", "availMemory", "threshold"]
            memoryValues = [memory['totalMemory'], memory['availMemory'], memory['threshold']]
            memoryColors = ["#F7464A", "#46BFBD", "#FDB45C"]

            pssLabels = ["dalvikPss", "nativePss", "otherPss", "totalPss"]
            pssValues = [memory['dalvikPss'], memory['nativePss'], memory['otherPss'], memory['totalPss']]
            pssColors = ["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA"]

            labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
            values = [10, 9, 8, 7, 6, 4, 7, 8]
            colors = ["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA", "#ABCDEF", "#DDDDDD", "#ABCABC"]

            return render_template('logdata_view.html', logdata=data, tagFilter=logDataTagSelection(),
                                   memorySet=zip(memoryValues, memoryLabels, memoryColors),
                                   pssSet=zip(pssValues, pssLabels, pssColors),
                                   set=zip(values, labels, colors))
    elif request.method == 'POST':
        jsonString = request.get_json()
        DBManager.logDataInsert(jsonString)
        return 'success'


@logdata.route('/logdatatagfilter/<string:tag>', methods=['GET'])
def logDataTagFilter(tag):
    if request.method == 'GET':
        data = DBManager.getLogDataTagFilter(tag)

        if data is None:
            return render_template('nodata.html')

        return render_template('logdata_view.html', logdata=data, tagFilter=logDataTagSelection())


def logDataTagSelection():
    projection = DBManager.getLogDataTagProjection()
    tagFilter = set()

    for item in projection:
        tagFilter.add(item['tag'])

    return tagFilter
