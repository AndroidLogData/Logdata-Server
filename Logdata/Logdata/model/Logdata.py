from mongoengine import Document, StringField, LongField, FloatField, IntField, BooleanField


class Logdata(Document):
    message = StringField()
    tag = StringField()
    level = StringField()
    time = LongField()
    totalMemory = LongField()
    availMemory = LongField()
    memoryPercentage = FloatField()
    threshold = LongField()
    lowMemory = BooleanField()
    dalvikPss = IntField()
    otherPss = IntField()
    totalPss = IntField()
