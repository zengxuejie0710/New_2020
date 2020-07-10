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
@pytest.mark.parametrize('a,b',yaml.safe_load(open("./testdata.yaml",encoding='utf-8')))
class Test_Calculator():
    @pytest.mark.add
    def test_add(self, cal,a, b):
        print("a+b",a+b)
        return a + b
    @pytest.mark.sub
    def test_sub(self,cal,a,b):
        print("a-b",a-b)
        return a - b
    @pytest.mark.div
    def test_div(self,cal, a, b):
        print("a-b",a/b)
        return a / b
    @pytest.mark.mul
    def test_mul(self,cal,a,b):
        print('a*b',a*b)
        return a * b

if __name__=="__main__":
    pytest.main(['-s', 'test_cal.py'])

