from req import RequestHandler
from req import reqenv

class CommitteesHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('../html/committees.html')
        return
    @reqenv
    def post(self):
        pass
