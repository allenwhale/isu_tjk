from req import RequestHandler
from req import reqenv

class VenueHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('../html/venue.html')
        return
    @reqenv
    def post(self):
        pass
