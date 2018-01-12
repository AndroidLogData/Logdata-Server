from flask import request, render_template
import json
from Logdata import DBManager
from Logdata.Log_Data_Blueprint import logdata


@logdata.route('/crash', methods=['GET', 'POST'])
def crash():
    if request.method == 'GET':
        temp = DBManager.getCrashData()

        display = json.loads(temp['Display'])
        build = json.loads(temp['Build'])
        deviceFeatures = json.loads(temp['DeviceFeatures'])

        deviceFeaturesitems = list()
        for item in deviceFeatures.items():
            deviceFeaturesitems.append(str(item[0]) + ' : ' + str(item[1]))

        data = {
            'Time': temp['Time'],
            'AndroidVersion': temp['AndroidVersion'],
            'APPVersionCode': temp['APPVersionCode'],
            'APPVersionName': temp['APPVersionName'],
            'AvailableMemorySize': temp['AvailableMemorySize'],
            'Brand': temp['Brand'],
            'Logcat': temp['Logcat'],
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
            'Build': temp['Build']
        }

        return render_template('crashdata_view.html', crashdata=data)
    elif request.method == 'POST':
        jsonString = request.get_json()
        print(jsonString)
        DBManager.crashDataInsert(jsonString)
        return 'success'
