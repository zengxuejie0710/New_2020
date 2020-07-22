# Author xuejie zeng
# encoding utf-8
from hogwarts.Homework_0719.weworklogin.index import Index


class TestReg():
    def setup(self):
        self.index = Index()

    def test_reg(self):
        #从首页调用去注册的方法，在调用注册方法。
        #思路是先把页面的信息即首页的PO写下不同的方法，然后每个PO点在创建不同的moudle,每个module里有对应的方法
        #使用的时候直接进行调用
        result = self.index.goto_register().regsiter()
        assert result

