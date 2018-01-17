import datetime
import json

from flask import request, render_template, jsonify

from Logdata.Log_Data_Blueprint import logdata
from Logdata.model.CrashData import CrashData


@logdata.route('/crash', methods=['GET', 'POST'])
def crash():
    if request.method == 'GET':
        # temp = DBManager.getCrashData()
        temp = CrashData.objects().first()

        # if temp.count() == 0:
        #     return render_template('nodata.html')
        if temp is None:
            return render_template('nodata.html')

        display = json.loads(temp.display)
        build = json.loads(temp.build)
        deviceFeatures = json.loads(temp.deviceFeatures)

        deviceFeaturesitems = list()
        for item in deviceFeatures.items():
            deviceFeaturesitems.append(str(item[0]) + ' : ' + str(item[1]))

        data = {
            'Time': temp.time,
            'AndroidVersion': temp.androidVersion,
            'APPVersionCode': temp.appVersionCode,
            'APPVersionName': temp.appVersionName,
            'AvailableMemorySize': temp.availableMemorySize,
            'Brand': temp.brand,
            'Logcat': temp.logcat,
            'Display': display['0']['realSize'],
            'Rotation': display['0']['rotation'],
            'Board': build['BOARD'],
            'BootLoader': build['BOOTLOADER'],
            'BuildBrand': build['BRAND'],
            'CPU_ABI': build['CPU_ABI'],
            'CPU_ABI2': build['CPU_ABI2'],
            'DisplayFirmware': build['DISPLAY'],
            'TWRP': build['DEVICE'],
            'Hardware': build['HARDWARE'],
            'Model': build['MODEL'],
            'DeviceFeatures': deviceFeaturesitems,
            'Build': temp.build
        }

        crashCount = []
        items = CrashData.objects().all()
        timeSet = set()

        for item in items:
            timeSet.add(str(item.time))

        timeSet = sorted(timeSet)
        print(timeSet)

        for item in timeSet:
            crashCount.append(CrashData.objects(time=item).all().count())

        print(crashCount)

        return render_template('crashdata_view.html', crashdata=data, values=zip(timeSet, crashCount))
    elif request.method == 'POST':
        jsonString = request.get_json()
        item = CrashData(datetime.datetime.strptime(jsonString['Time'], '%Y-%m-%d %H:%M:%S'),
                         jsonString['AndroidVersion'],
                         jsonString['APPVersionCode'],
                         jsonString['APPVersionName'],
                         jsonString['AvailableMemorySize'],
                         jsonString['Brand'],
                         jsonString['Logcat'],
                         jsonString['DeviceID'],
                         jsonString['Display'],
                         jsonString['Environment'],
                         jsonString['DeviceFeatures'],
                         jsonString['Build'])
        item.save()
        return jsonify({'result': 'success'})
