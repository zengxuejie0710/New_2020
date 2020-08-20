# Author xuejie zeng
# encoding utf-8

import requests
import pytest
class Util:
    def get_token(self):
        """
        获取token
         https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww1cfe02ff5dc2522a&corpsecret=-DNMkpbtJdncAuQ15DqZAxEdaNM88oEZADuHJAnZIts
        :return:
        """
        request_para = {
            "corpid": "ww1cfe02ff5dc2522a",
            "corpsecret": "-DNMkpbtJdncAuQ15DqZA55yzbLjJYDP8hkSkySWOAo"
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=request_para)
        print(r.json()["access_token"])
        return r.json()['access_token']