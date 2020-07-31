# Author xuejie zeng
# encoding utf-8
import time

from hogwarts.Homework_0726.basepage.base import Base
from hogwarts.Homework_0726.page.addcontext import AddContext
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class  Add_Input(Base):
    input_click = (MobileBy.XPATH,"//*[@text='手动输入添加']")
    toast_ele = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
    def addinput(self):
        """
        点击手动输入添加
        :return:
        """
        time.sleep(3)
        self.click_element(self.input_click)
        return AddContext(self.driver)

    def get_toast(self):
        # text = '成功'
        # element = WebDriverWait(self.driver, 10).until(
        #     lambda x: x.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        element = self.webdriver_wait(self.toast_ele)
        result = element.text
        return result

