# coding: utf-8

from .BaseHandler import BaseHandler

class IndexHander(BaseHandler):
	def get(self):
		self.write("hello");