# Author xuejie zeng
# encoding utf-8
from hogwarts.Homework_0726.basepage.base import Base
from hogwarts.Homework_0726.page.mainpage import MainPage
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

class APP(Base):
        def start(self):
            if self.driver == None:
                caps = {}
                caps["platformName"] = "android"
                caps["deviceName"] = "5eb2803"
                caps["appPackage"] = "com.tencent.wework"
                caps["appActivity"] =".launch.LaunchSplashActivity"
                caps["noReset"] = "true"
                caps["platformVersion"] = "7.1.1"
                caps['unicodeKeyboard'] = 'true'
                caps['resetKeyboard'] = 'true'
                caps['automationName'] = 'uiautomator2'
                self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            else:
                self.driver.launch_app()
            self.driver.implicitly_wait(5)
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