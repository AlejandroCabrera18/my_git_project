import jinja2
import webapp2
import os
import models

from models import Search

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class HomePage(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/mainpage.html')
        self.response.write(result_template.render())
    def post(self):
        result_template = the_jinja_env.get_template('templates/mainpage.html')
        self.response.write(result_template.render())

class ResultsPage(webapp2.RequestHandler):
    def post(self):
        result_template = the_jinja_env.get_template('templates/result.html')
        zip_code = self.request.get("zip_code")
        address = self.request.get("address")
        activity = self.request.get("activity")
        data = Search(zip_code=zip_code,address=address,activity=activity)
        search_data = {
            "address": address,
            "zip_code":zip_code,
            "activity": activity
        }
        self.response.write(result_template.render(search_data))


app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/results', ResultsPage) #this maps the root url to the Main Page Handler
], debug=True)
