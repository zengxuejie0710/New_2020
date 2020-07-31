# Author xuejie zeng
# encoding utf-8
from appium.webdriver.common.mobileby import MobileBy

from hogwarts.Homework_0726.basepage.base import Base
from hogwarts.Homework_0726.page.contlist import ContList


class Serch_Page(Base):
    serch = (MobileBy.ID,'com.tencent.wework:id/hib')

    def serchpage(self):
        """
        进入搜索框页面
        :return:
        """
        #点击搜索框
        self.click_element(self.serch)

        return ContList(self.driver)
