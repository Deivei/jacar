import tornado.web

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])

class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width =self.get_grgument('width', 40)
        self.write(textwrap.fill(text, int(width)))
