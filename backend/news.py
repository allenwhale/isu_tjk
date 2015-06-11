from req import RequestHandler
from req import reqenv

class NewsHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('../html/news.html')
        return
    @reqenv
    def post(self):
        pass
