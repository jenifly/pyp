#coding: utf-8

import os

# Application 配置参数
settings = {
	"static_path": os.path.join(os.path.dirname(__file__), "static"),
	"template_path": os.path.join(os.path.dirname(__file__), "template"),
	"cookie_secret": "sgfhg5j+tres4sghjf8vvbb2dsavcop=",
	"xsrf_cookies": True,
	"debug": True,
}

# mysql
mysql_options = dict(
	host="127.0.0.1",
	database="ihome",
	user="root",
	password="root"
)

# redis
redis_options = dict(
	host="127.0.0.1",
	port=6379
)