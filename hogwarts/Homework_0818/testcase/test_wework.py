# Author xuejie zeng
# encoding utf-8
from hogwarts.Homework_0818.api.wework import WeWork


class TestWework:
    def test_get_token(self):
        print(WeWork().test_get("ZengXueJie"))

    def test_creat(self):
        print(WeWork().test_create("zxj01", 'zeng', '17837898889'))

    def test_get(self):
        print(WeWork().test_get("zxj01"))

    def test_updata(self):
        print(WeWork().test_get_update("zxj01",'zdj'))

    def test_delete(self):
        print(WeWork().test_delete("zxj01"))
