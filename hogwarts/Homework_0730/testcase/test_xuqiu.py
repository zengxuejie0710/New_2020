# Author xuejie zeng
# encoding utf-8
from hogwarts.Homework_0730.app.app import App


class TestXueqiu:
    def setup(self):
        self.app = App()


    def test_01(self):
        self.app.start().goto_index().goto_market()
        # search.search('阿里巴巴')
        # assert search.is_choose('阿里巴巴')

