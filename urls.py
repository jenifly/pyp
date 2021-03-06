# coding: utf-8

import os

from handlers import Passport, VerifyCode
from handlers.BaseHandler import StaticFileBaseHandler as StaticFileHandler

handlers = [
    #(r"/", Passport.IndexHander),
    (r"/api/imagecode", VerifyCode.ImageCodeHandler),
    (r"/(.*)", StaticFileHandler,
    dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename="index.html"))
]