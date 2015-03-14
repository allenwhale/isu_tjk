from req import RequestHandler
from req import reqenv

class CallforpaperHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('../html/callforpaper.html')
        return
    @reqenv
    def post(self):
        pass
