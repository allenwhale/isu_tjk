from req import RequestHandler
from req import reqenv

class HomeHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('../html/home.html')
        pass
    @reqenv
    def post(self):
        pass