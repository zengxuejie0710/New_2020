# Author xuejie zeng
# encoding utf-8
import random
import re

import requests
import pytest
import xdist #分布式运行

def test_creat_data():
    # data = [(str(random.randint(0, 9999999)), '小可爱',
    #          str(random.randint(13800000000, 13899999000))) for x in range(3)]
    data = [('zxj' + str(x), '小可爱',
             "138%08d"% x) for x in range(10)]
    # print(data)
    return data

class TestWework:

    @pytest.fixture(scope="session")
    def token(self):
        """
        获取token
         https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww1cfe02ff5dc2522a&corpsecret=-DNMkpbtJdncAuQ15DqZAxEdaNM88oEZADuHJAnZIts
        :return:
        """
        request_para = {
            "corpid":"ww1cfe02ff5dc2522a",
            "corpsecret":"-DNMkpbtJdncAuQ15DqZAxEdaNM88oEZADuHJAnZIts"
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",params= request_para)
        return r.json()['access_token']

    def test_create(self,token,userid,name,mobile,department = None):
        """
        创建成员
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        if department == None:
            department = [1]

        request_body={
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
                      json= request_body)
        return r.json()

    def test_get(self,token,userid):
        """
        查看成员
        https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """

        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}")
        return r.json()

    def test_get_update(self,token,userid,name):
        """
        更新成员信息
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        request_body = {
            "userid": userid,
            "name": name,
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",
                      json=request_body)
        return r.json()

    def test_delete(self,token,userid):
        """
        删除成员
        :return:
        """
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}")
        return r.json()

    @pytest.mark.parametrize("userid,name,mobile",test_creat_data())
    def test_total(self,token,userid,name,mobile):
        """
        整体流程测试
        :return:
        """
        # userid = 'xiaokeai2'
        # name = '小可爱哟'
        # mobile = '13200000001'
        try:
            assert "created" == self.test_create(token,userid,name,mobile)["errmsg"]
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                re_userid = re.findall(":(.*)'$",e.__str__())[0] #只取第一个
                self.test_delete(token, re_userid)
                assert "created" == self.test_create(token, userid, name, mobile)["errmsg"]
        assert name == self.test_get(token,userid)["name"]
        assert "updated" == self.test_get_update(token,userid,name)["errmsg"]
        assert name == self.test_get(token,userid)["name"]
        assert "deleted" == self.test_delete(token,userid)["errmsg"]
        assert 60111 == self.test_get(token,userid)["errcode"]

