# from mongoengine import Document, StringField, LongField, FloatField, IntField, BooleanField
#
#
# class Logdata(Document):
#     message = StringField()
#     tag = StringField()
#     level = StringField()
#     time = LongField()
#     totalMemory = LongField()
#     availMemory = LongField()
#     memoryPercentage = FloatField()
#     threshold = LongField()
#     lowMemory = BooleanField()
#     dalvikPss = IntField()
#     otherPss = IntField()
#     totalPss = IntField()

from flask_mongoalchemy import Document
from mongoalchemy.fields import IntField, BoolField, FloatField, StringField


class Logdata(Document):
    def __init__(self, message, tag, level, time, totalMemory, availMemory, memoryPercentage, threshold, lowMemory,
                 dalvikPss, otherPss, totalPss, **kwargs):
        super().__init__(**kwargs)
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
        self.otherPss = otherPss
        self.totalPss = totalPss

    message = StringField()
    tag = StringField()
    level = StringField()
    time = IntField()
    totalMemory = IntField()
    availMemory = IntField()
    memoryPercentage = FloatField()
    threshold = IntField()
    lowMemory = BoolField()
    dalvikPss = IntField()
    otherPss = IntField()
    totalPss = IntField()
