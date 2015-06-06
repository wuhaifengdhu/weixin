# encode = utf-8
__author__ = 'haifwu@ebay.com'

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading
import hashlib
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

class Handler(BaseHTTPRequestHandler):
    

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    port = 80
    address = ('', port)
    server = ThreadedHTTPServer(address, Handler)
    print 'Server is running at http://127.0.0.1:%s' % port
    print 'Start server, use <Ctrl + C> to stop'
    server.serve_forever()

















