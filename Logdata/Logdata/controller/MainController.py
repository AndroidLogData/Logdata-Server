from flask import render_template
from Logdata.Log_Data_Blueprint import logdata
from Logdata.model.LogData import LogData


@logdata.route('/')
def index():
    try:
        # data = Logdata.objects().fields(packageName=1)
        items = LogData.objects().all()
        values = set()

        if items.count() == 0:
            return render_template('main.html')

        for item in items:
            values.add(item.packageName)

        return render_template('main.html', values=values)
    except Exception as e:
        print(e)
