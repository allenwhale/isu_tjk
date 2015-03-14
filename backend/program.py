from req import RequestHandler
from req import reqenv

class ProgramHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('../html/program.html')
        return

    @reqenv
    def post(self):
        pass
