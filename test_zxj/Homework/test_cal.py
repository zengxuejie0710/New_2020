# 1、补全计算器（加减乘除）的测试用例
#
# 2、使用数据驱动完成测试用例的自动生成
#
# 3、conftest.py中创建fixture 完成setup和teardown
#
# 4、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 被测模块
# 实现计算器

import pytest
import yaml
from test_zxj.Homework.comm import cal

###使用不同的账号进行登录######
@pytest.mark.parametrize('login', [('username', 'passwd'),("zzz","jjj")], indirect=True)
class TestLogin():

    def setup_class(self):
        print("我是登录前的操作")
    def test_login(self,login):
        a = login
        print("返回值%s"%a)
        assert a,"失败原因：账号不正确"
    def teardown_class(self):
        print("我是登录后的操作")

######计算器开始计算的测试用例######
@pytest.mark.parametrize("param_a",yaml.safe_load(open("./testdata.yaml",encoding='utf-8')),indirect=True,ids=[
    "正整数",
    "小数"
])
@pytest.mark.parametrize("param_b",yaml.safe_load(open("./testdata.yaml",encoding='utf-8')),indirect=True,ids=[
    "小数",
    "数值为0"
])

class Test_Calculator():
    cal = cal.Calculator()
    @pytest.mark.add
    def test_add(self, param_a,param_b):
        a=param_a
        b=param_b
        print("a+b",a+b)
        result=a+b
        assert result == self.cal.add(a,b)
    @pytest.mark.sub
    def test_sub(self,param_a,param_b):
        a=param_a
        b=param_b
        print("a+b",a-b)
        result=a-b
        assert result == self.cal.sub(a,b)
    @pytest.mark.div
    def test_div(self,param_a,param_b):
        a=param_a
        b=param_b
        # print("a+b",a / b)
        try:
            result = a / b
            assert result == self.cal.div(a,b)
        except :
            return "除数不能为0"
    @pytest.mark.mul
    def test_mul(self,param_a,param_b):
        a=param_a
        b=param_b
        print("a+b",a * b)
        result=a * b
        assert result == self.cal.mul(a,b)

if __name__=="__main__":
    pytest.main(['-s', 'test_cal.py'])

