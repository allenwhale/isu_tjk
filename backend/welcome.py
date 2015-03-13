from req import RequestHandler
from req import reqenv

class WelcomeHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('../html/welcome.html')
        pass
    @reqenv
    def post(self):
        pass
