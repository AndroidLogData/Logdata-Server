from mongoengine import *


class LogData(Document):
    def __init__(self, packageName, message, tag, level, time, totalMemory, availMemory, memoryPercentage, threshold,
                 lowMemory, dalvikPss, nativePss, otherPss, totalPss, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.packageName = packageName
        self.message = message
        self.tag = tag
        self.level = level
        self.time = time
        self.totalMemory = totalMemory
        self.availMemory = availMemory
        self.memoryPercentage = memoryPercentage
        self.threshold = threshold
        self.lowMemory = lowMemory
        self.dalvikPss = dalvikPss
        self.nativePss = nativePss
        self.otherPss = otherPss
        self.totalPss = totalPss

    packageName = StringField(required=True)
    message = StringField(required=True)
    tag = StringField(required=True)
    level = StringField(required=True)
    time = DateTimeField(required=True)
    totalMemory = IntField()
    availMemory = IntField()
    memoryPercentage = FloatField()
    threshold = IntField()
    lowMemory = BooleanField()
    dalvikPss = IntField()
    nativePss = IntField()
    otherPss = IntField()
    totalPss = IntField()
    meta = {'allow_inheritance': True}
