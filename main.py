import webapp2

class MainHandler(webapp2.RequestHandler):

  def get(self, *args, **kwargs):
    self.redirect('//' + self.request.host + '/ioxkl16/')

app = webapp2.WSGIApplication([
    ('/ioxkl16.*', MainHandler),
], debug=True)