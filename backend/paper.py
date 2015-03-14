from req import RequestHandler
from req import reqenv

class PaperHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('../html/paper.html')
        return
    @reqenv
    def post(self):
        pass
