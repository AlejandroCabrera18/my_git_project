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
        age = int(self.request.get("age"))
        mode_of_transportation = self.request.get("mode of travel")
        range = int(self.request.get("distance"))
        location = self.request.get("location")
        data = Search(age=age,mode_of_transportation=mode_of_transportation,range=range,location=location)
        data.put()
        search_data = {
            "age": age,
            "transportation": mode_of_transportation,
            "range": range,
            "location": location
        }
        self.response.write(result_template.render(search_data))


app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/results', ResultsPage) #this maps the root url to the Main Page Handler
], debug=True)
