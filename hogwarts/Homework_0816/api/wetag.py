# Author xuejie zeng
# encoding utf-8

import requests
import yaml
import pytest
from hogwarts.Homework_0816.api.baseapi import BaseApi
from hogwarts.Homework_0816.api.util import Util

#标签管理
class WeTag(BaseApi):

    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token
        with open("../api/wetag.yaml", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def test_create(self, tagname,tagid):
        """
        创建标签
        https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=ACCESS_TOKEN
        :return:
        """
        self.params["tagname"] = tagname
        self.params["tagid"] = tagid
        return self.send(self.data["create"])


    def test_get(self, tagid):
        """
        获取标签成员
        https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token=ACCESS_TOKEN&tagid=TAGID
        :return:
        """
        self.params["tagid"] = tagid
        return self.send(self.data["get"])

    def test_get_update(self, tagid,tagname):
        """
        更新标签信息
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        self.params["tagid"] = tagid
        self.params["tagname"] = tagname
        return self.send(self.data["update"])

    def test_delete(self, tagid):
        """
        删除标签
        https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=ACCESS_TOKEN&tagid=TAGID
        :return:
        """
        self.params["tagid"] = tagid
        return self.send(self.data["delete"])