from application.app import mongo

class BTC(mongo.Document):
    time = mongo.DateTimeField()
    open = mongo.FloatField()
    high = mongo.FloatField()
    low = mongo.FloatField()
    close = mongo.FloatField()

    def __repr__(self):
        return '<BTC %r>' % self.__class__
