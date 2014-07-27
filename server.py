import urls

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
define('port', default=8000, help='run on the given', type=int)

tornado.options.parse_command_line()
app = tornado.web.Application(urls.urls)
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()
