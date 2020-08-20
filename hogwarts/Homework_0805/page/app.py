# Author xuejie zeng
# encoding utf-8

from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from hogwarts.Homework_0805.page.base_page import BasePage
from hogwarts.Homework_0805.page.main import Main


class App(BasePage):
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
                # caps['settings[waitForIdleTimeout]'] = 0
                self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            else:
                self.driver.launch_app()
            self.driver.implicitly_wait(10)
            #回到这个页面的目的是为了调用该也页面下的其他函数，如果不返回self则不能调用到goto_index这个函数
            return self

        def goto_main(self):
            """
            进入首页
            :return:
            """
            return Main(self.driver)