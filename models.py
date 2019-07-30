from google.appengine.ext import ndb

class search(ndb.Model):
    age = ndb.IntegerProperty(required=False)
    mode_of_transportation=ndb.StringProperty(required=True)
    range = ndb.IntegerProperty(required=True)
