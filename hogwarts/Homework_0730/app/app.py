# Author xuejie zeng
# encoding utf-8

from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from hogwarts.Homework_0730.basepage.base import Base
from hogwarts.Homework_0730.page.mainpage import MainPage


class App(Base):
        def start(self):
            if self.driver == None:
                caps = {}
                caps["platformName"] = "android"
                caps["deviceName"] = "b427c1d6"
                caps["appPackage"] = "com.xueqiu.android"
                caps["appActivity"] =".view.WelcomeActivityAlias"
                caps["noReset"] = "true"
                caps["platformVersion"] = "10"
                caps['unicodeKeyboard'] = 'true'
                caps['resetKeyboard'] = 'true'
                caps['automationName'] = 'uiautomator2'
                self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            else:
                self.driver.launch_app()
            self.driver.implicitly_wait(7)
            #回到这个页面的目的是为了调用该也页面下的其他函数，如果不返回self则不能调用到goto_index这个函数
            return self

        def goto_index(self):
            """
            进入到首页
            :return:
            """
            return MainPage(self.driver)

        def app_quit(self):
            """
            关闭app
            :return:
            """
            self.driver.quit()