# Author xuejie zeng
# encoding utf-8
from hogwarts.Homework_0726.basepage.base import Base
from hogwarts.Homework_0726.page.contlist import ContList
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.mobileby import MobileBy

from hogwarts.Homework_0726.page.serch_page import Serch_Page


class MainPage(Base):

    contact = (MobileBy.XPATH,"//*[@text='通讯录']")

    def goto_cont(self):
        """
        进入通讯录
        :return:
        """
        self.click_element(self.contact)
        return ContList(self.driver)

    def add_member(self):
        """
        进入添加成员页面
        :return:
        """
        pass

    def goto_inputmember(self):
        """
        手动输入成员信息
        :return:
        """
        pass