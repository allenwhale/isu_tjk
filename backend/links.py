from req import RequestHandler
from req import reqenv

class LinksHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('../html/links.html')
        return
    @reqenv
    def post(self):
        pass
