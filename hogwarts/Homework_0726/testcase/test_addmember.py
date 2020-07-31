# Author xuejie zeng
# encoding utf-8
import yaml

from hogwarts.Homework_0726.app.app import APP
import pytest


with open("../yaml/testdata.yml",encoding="utf-8") as f:
    getdata = yaml.safe_load(f)


with open("../yaml/deledata.yml",encoding="utf-8") as f:
    deldata = yaml.safe_load(f)

class TestCase:

    def setup(self):
        self.app = APP()
        self.main = self.app.start().goto_index()
    def teardown(self):
        self.app.app_quit()

    @pytest.mark.parametrize("filename,phonenum",getdata)
    def test_01(self,filename,phonenum):

        result=self.main.goto_cont().click_addmember().addinput().set_name(filename).set_sex().set_phone(phonenum).click_save()
        gettext = result.get_toast()
        assert '成功' in gettext

    @pytest.mark.parametrize("name",deldata)
    def test_02(self,name):
        self.myserch = self.main.goto_cont().serchpage()
        self.mylist =self.myserch.serch_name(name)
        self.mypage =self.myserch.list_data(self.mylist).per_info().editmem().delmember()
        self.deleafter = self.myserch.serch_name(name)
        assert len(self.mylist) -len(self.deleafter) == 1


