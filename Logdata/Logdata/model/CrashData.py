from mongoengine import *


class CrashData(Document):
    def __init__(self, time, androidVersion, appVersionCode, appVersionName, availableMemorySize, brand, logcat,
                 deviceID, display, environment, deviceFeatures, build, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.time = time
        self.androidVersion = androidVersion
        self.appVersionCode = appVersionCode
        self.appVersionName = appVersionName
        self.availableMemorySize = availableMemorySize
        self.brand = brand
        self.logcat = logcat
        self.deviceID = deviceID
        self.display = display
        self.environment = environment
        self.deviceFeatures = deviceFeatures
        self.build = build

    time = DateTimeField(required=True)
    androidVersion = StringField()
    appVersionCode = StringField()
    appVersionName = StringField()
    availableMemorySize = StringField()
    brand = StringField()
    logcat = StringField()
    deviceID = StringField()
    display = StringField()
    environment = StringField()
    deviceFeatures = StringField()
    build = StringField()
    meta = {'allow_inheritance': True}
