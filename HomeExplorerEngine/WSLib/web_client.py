__author__ = 'sdeni'
import requests

class ExplorerEngineError(Exception):
    def __init__(self, msg, code, response):
        self.msg = msg
        self.error_code = code
        self.responce = response
    def __str__(self):
        return repr('%s: %s %s' % (self.error_code, self.msg, self.responce))

class EngineActions():
    def __init__(self):
        self.controller_url = "http://127.0.0.1:5000/"
        self.client = requests.Session()
        self.method = 'GET'

    def call(self, path, **kwargs):
        try:
            url = self.controller_url + path
            response = self.client.request(self.method, url)
            pass
        except requests.RequestException:
            raise

        code = response.status_code

        if not 200 <= code < 300:
            raise ExplorerEngineError(response.content, code, response)

        # parse response:

    def forward(self):
        path = "action/v1.0/forward"
        self.call(path=path)

    def backward(self):
        path = "action/v1.0/backward"
        self.call(path=path)

    def stop(self):
        path = "action/v1.0/stop"
        self.call(path=path)