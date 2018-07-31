import tornado.ioloop
from tornado.web import *
from server.handler import *
from server.handler.RespObj import RespObj
import json


class BaseHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def return_json(self, obj):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True)
        #escape.json_encode(RespObj.return_ok(obj = obj))


if __name__ == "__main__":
    pass
