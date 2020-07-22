# Author xuejie zeng
# encoding utf-8
from hogwarts.Homework_0719.wework import index_one


class TestAddM():

    def setup(self):
        self.indexone = index_one.IndexOne()

    def test_addm(self):
        self.indexone.goto_member().add_member()