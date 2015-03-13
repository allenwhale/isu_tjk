import tornado.ioloop
import tornado.web 
from req import Service
from req import reqenv
from req import RequestHandler
from home import HomeHandler
from welcome import WelcomeHandler

import pg

class IndexHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('../html/index_1.html',page = 'index')
        return 


if __name__ == '__main__':
    #db = pg.AsyncPG('web','admin','adminpassword',dbtz='+8')
    app = tornado.web.Application([
        ('/', IndexHandler),
        ('/home', HomeHandler),
        ('/welcome', WelcomeHandler),
        ('/(.*)', tornado.web.StaticFileHandler, {'path':'../html/'}),
        ],cookie_secret = 'cookie',autoescape = 'xhtml_escape')
    app.listen(888)
    tornado.ioloop.IOLoop.instance().start()
