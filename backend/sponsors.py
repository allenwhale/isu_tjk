from req import RequestHandler
from req import reqenv

class SponsorsHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('../html/sponsors.html')
        return
    @reqenv
    def post(self):
        pass
