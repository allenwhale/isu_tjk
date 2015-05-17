from req import reqenv
from req import RequestHandler

class AboutHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('../html/about.html')
        return
