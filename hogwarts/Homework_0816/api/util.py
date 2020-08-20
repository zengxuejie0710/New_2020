# Author xuejie zeng
# encoding utf-8

import requests
import yaml

class Util():
    def get_token(self):
        """
        获取token
         https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww1cfe02ff5dc2522a&corpsecret=-DNMkpbtJdncAuQ15DqZAxEdaNM88oEZADuHJAnZIts
        :return:
        """
        with open("../datas/wetag.yaml", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=data["get_token"])
        return r.json()['access_token']