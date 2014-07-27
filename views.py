import tornado.web

class Hello(tornado.web.RequestHandler):
    def get(self):
        greetings= self.get_argument('greetings', 'hello')
        self.write(greetings + ',dewei!')

