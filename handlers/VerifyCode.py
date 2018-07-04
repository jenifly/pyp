# coding utf-8

import logging

from constants import IMAGE_CODE_EXPIRES_SENCONDS
from .BaseHandler import BaseHandler
from utils.captcha.captcha import captcha
from utils.response_code import RET

class ImageCodeHandler(BaseHandler):

    def get(self):
        self.redis.setex("image_code_432", "120", "text")
        code_id = self.get_argument("codeid")
        pre_code_id = self.get_argument("pcodeid")
        if pre_code_id:
            try: 
                self.redis.delete("pic_code_%s" % pre_code_id)
            except Exception as e:
                logging.error(e)
        name, text, image = captcha.generate_captcha()
        try:
            self.redis.setex("image_code_%s" % code_id, IMAGE_CODE_EXPIRES_SENCONDS, text)
            print("redis_yes")
        except Exception as e:
            logging.error(e)
            self.write("")
            print("redis_no")
        self.set_header("Content-Type", "image/jpg")
        self.write(image)

class CodeHandler(BaseHandler):
    def post(self):
        image_code_id = self.json_args.get("image_code_id")
        image_code_text = self.json_args.get("imqge_code_text")

        if all((image_code_id, image_code_text)):
            return self.write(dict(errno=RET.PARAMERR, errmsg="参数缺失"))

        # 获取图片验证码真实值
        try:
            real_image_code_text = self.redis.get("image_code_%s" % image_code_id)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errcode=RET.DBERR, errmsg="查询验证码错误"))
        if not real_image_code_text:
            return self.write(dict(errcode=RET.NODATA, errmsg="验证码过期"))

        # 删除图片验证码
        try:
            self.redis.delete("pic_code_%s" % image_code_id)
        except Exception as e:
            logging.error(e)

        # 校验验证码
        if real_image_code_text.lower() != image_code_text.lower():
            return self.write(dict(errcode=RET.DATAERR, errmsg="验证码错误"))