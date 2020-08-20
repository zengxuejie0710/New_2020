# Author xuejie zeng
# encoding utf-8
from selenium.webdriver.common.by import By

from hogwarts.Homework_0730.basepage.base import Base
from appium.webdriver.common.mobileby import MobileBy

from hogwarts.Homework_0730.page.search import SearchPage


class MainPage(Base):
    #使用and组合定位
    #market = (MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='行情']")
    #使用父节点组合定位

    def goto_market(self):
        """
        进入行情
        :return:
        """
        #伪造黑名单
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        self.find(By.XPATH,"//*[@resource-id='android:id/tabs']/..//*[@text='行情']").click()

        return SearchPage(self.driver)

