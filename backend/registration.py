from req import RequestHandler
from req import reqenv

class RegistrationHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('../html/registration.html')
        return
    @reqenv
    def post(self):
        pass
