import webapp2

from google.appengine.ext.webapp import template
import os

# REQUEST HANDLERS:
class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = { }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))
   
class Channel(webapp2.RequestHandler):
    def get(self):
        template_values = { }

        path = os.path.join(os.path.dirname(__file__), 'channel.html')
        self.response.out.write(template.render(path, template_values))
   

application = webapp2.WSGIApplication([('/', MainPage), ('/channel.html', Channel)],
                                        debug=True)

