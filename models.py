from google.appengine.ext import ndb

class Search(ndb.Model):
    address=ndb.StringProperty(required=True)
    zip_code=ndb.StringProperty(required=True)
    activity=ndb.StringProperty(required=True)
