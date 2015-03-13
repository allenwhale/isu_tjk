from req import RequestHandler
from req import reqenv

class HomeHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('../html/home.html')
        return
    @reqenv
    def post(self):
        pass
