# Author xuejie zeng
# encoding utf-8
import time

from hogwarts.Homework_0726.basepage.base import Base
from hogwarts.Homework_0726.page.addmember import Add_Input
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from hogwarts.Homework_0726.page.personlist import PersonPage


class ContList(Base):
    click_member = (MobileBy.XPATH,"//*[@text='添加成员']")
    # member_one = (MobileBy.XPATH,'//*[@text="{name}"]')
    serch_input = (MobileBy.ID,'com.tencent.wework:id/g5b')
    serch = (MobileBy.ID,'com.tencent.wework:id/hib')

    def click_addmember(self):
        """
        点击添加成员
        :return:
        """
        self.click_element(self.click_member)
        return Add_Input(self.driver)

    def serchpage(self):
        """
        进入搜索框页面
        :return:
        """
        #点击搜索框
        self.click_element(self.serch)
        return self

    def serch_name(self,name):
        """
        点击删除成员
        :return:
        """
        #输入姓名
        self.find_and_sendkeys(self.serch_input,name)
        #模糊查询输入的姓名
        self.getlist=(MobileBy.XPATH, f"//*[contains(@text,'{name}')]")
        time.sleep(3)
        #获取联系人列表
        self.listele = self.finds(self.getlist)
        print("找的列表",len(self.listele))
        return self.listele

    def list_data(self,listele):
        print("在这个函数里的数据",len(listele))
        if len(listele) >= 1:
            print("要点击的数据",self.listele[1].text)
            # self.click_element(self.listele[0])
            self.listele[1].click()
        else:
            print("没有找到联系人")
            return
        return PersonPage(self.driver)






