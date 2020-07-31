# Author xuejie zeng
# encoding utf-8
from hogwarts.Homework_0726.basepage.base import Base
from appium.webdriver.common.mobileby import MobileBy

from hogwarts.Homework_0726.page.deletemember import DeleMember


class EditMember(Base):

    editmemb = (MobileBy.ID,"com.tencent.wework:id/b4g")

    def editmem(self):
        """
        点击编辑成员按钮
        :return:
        """
        self.click_element(self.editmemb)
        return DeleMember(self.driver)