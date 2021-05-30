import copy
import json
import os
import pathlib
import re
import subprocess
import sys
from http.server import CGIHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HTTP_SERVER_PORT = 7777


def urlToPath(url):
    if sys.platform == 'win32':
        return str(pathlib.Path(url).absolute())
    else:
        return url


def pathToUrl(filepath=''):
    if sys.platform == 'win32':
        return pathlib.Path(filepath).absolute().as_uri().split(':')[2][1:]
    else:
        return str(pathlib.Path(filepath).absolute())[1:]


class HTTPServerHandler(CGIHTTPRequestHandler):

    def do_GET(self):
        """
        Handling GET requests
        """
        arr = [1,2,3,4,5,6,7,8,9,0, -14, -20, -44]
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(arr).encode())


server = ThreadingHTTPServer(('127.0.0.1', HTTP_SERVER_PORT), HTTPServerHandler)

server.server_name = '127.0.0.1'
server.server_port = HTTP_SERVER_PORT

try:
    print("start http server")
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()
