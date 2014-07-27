from views import *
from tornado import web

urls = [
        (r'/reverse/(\w+)', ReverseHandler),
        (r'/wrap', WrapHandler)
         ]
