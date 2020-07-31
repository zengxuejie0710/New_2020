# Author xuejie zeng
# encoding utf-8
from hogwarts.Homework_0726.basepage.base import Base
from appium.webdriver.common.mobileby import MobileBy

from hogwarts.Homework_0726.page.editmember import EditMember


class PersonPage(Base):

    right_up = (MobileBy.ID,"com.tencent.wework:id/hi2")

    def per_info(self):
        """
        点击右上角的按钮
        :return:
        """
        self.click_element(self.right_up)
        return EditMember(self.driver)