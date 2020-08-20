# Author xuejie zeng
# encoding utf-8

import requests
import yaml
import pytest
from hogwarts.Homework_0818.api.baseapi import BaseApi
from hogwarts.Homework_0818.api.util import Util

#成员管理
class WeWork(BaseApi):

    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token
        with open("../api/wework.yaml",encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def test_create(self, userid, name, mobile, department=None):
        """
        创建成员
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        if department == None:
            department = "1"
        # request_body = {
        #     "userid": userid,
        #     "name": name,
        #     "mobile": mobile,
        #     "department": department
        # }
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
        #                   json=request_body)
        # data = {
        #     "method":"post",
        #     "url":f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
        #     "json":
        #         {
        #             "userid": userid,
        #             "name": name,
        #             "mobile": mobile,
        #             "department": department
        #         }
        # }

        self.params["userid"] = userid
        self.params["name"] = name
        self.params["mobile"] = mobile
        self.params["department"] = department

        return self.send(self.data["create"])

    def test_get(self, userid):
        """
        查看成员
        https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}")
        # data = {
        #     "method" : "get",
        #     "url" : f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        # }

        self.params["userid"] = userid
        return self.send(self.data["get"])


    def test_get_update(self, userid, name):
        """
        更新成员信息
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        # request_body = {
        #     "userid": userid,
        #     "name": name,
        # }
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
        #                   json=request_body)
        # data = {
        #     "method" : "post",
        #     "url" :f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
        #     "json" :
        #             {
        #         "userid": userid,
        #         "name": name,
        #     }
        # }
        self.params["userid"] = userid
        self.params["name"] = name

        return self.send(self.data["update"])

    def test_delete(self, userid):
        """
        删除成员
        :return:
        """
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}")
        # data = {
        #     "method" : "get",
        #     "url" : f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        # }
        self.params["userid"] = userid

        return self.send(self.data["delete"])