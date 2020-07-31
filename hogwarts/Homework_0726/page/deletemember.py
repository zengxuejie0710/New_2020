# Author xuejie zeng
# encoding utf-8
from hogwarts.Homework_0726.basepage.base import Base
from appium.webdriver.common.mobileby import MobileBy


class DeleMember(Base):

    delsroll = "删除成员"
    surebutton = (MobileBy.ID,"com.tencent.wework:id/ber")
    def delmember(self):
        """
        点击删除成员
        :return:
        """
        self.find_by_scroll(self.delsroll).click()
        self.click_element(self.surebutton)
