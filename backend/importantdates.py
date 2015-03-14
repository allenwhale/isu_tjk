from req import RequestHandler
from req import reqenv

class ImportantdatesHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('../html/importantdates.html')
        return
    @reqenv
    def post(self):
        pass
