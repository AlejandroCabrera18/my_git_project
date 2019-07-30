import jinja2
import webapp2
import os
import models

from models import search

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class HomePage(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/mainpage.html')
        search_data={}
        self.response.write(result_template.render(search_data))
    def post(self):
        result_template = the_jinja_env.get_template('templates/mainpage.html')
        search_data={}
        self.response.write(result_template.render(search_data))

class ResultsPage(webapp2.RequestHandler):
    def post(self):
        result_template = the_jinja_env.get_template('templates/resultpage.html')
        age = self.request.get("age")
        mode_of_transportation = self.request.get("mode of travel")
        range = self.request.get("distance")
        data = search(age=age,mode_of_transportation=mode_of_transportation,range=range)
        search.put()
        search_data = {
            "age": age,
            "transportation": mode_of_transportation,
            "range": range
        }
        self.response.write(result_template.render(search_data))


app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/results', ResultsPage) #this maps the root url to the Main Page Handler
], debug=True)
