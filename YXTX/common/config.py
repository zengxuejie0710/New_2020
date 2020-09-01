# coding:utf-8
import time

from YXTX.common.base import Base
from appium import webdriver

from YXTX.page.order import SearchOrder


class App(Base):
    """
    壹行天下app配置
    :return:
    """
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "b427c1d6"
            caps["appPackage"] = "io.dcloud.H5A6DF4A7"
            caps["appActivity"] = "io.dcloud.H5A6DF4A7.MainActivity"
            caps["noReset"] = "true"
            caps["platformVersion"] = "10"
            caps['unicodeKeyboard'] = 'true'
            caps['resetKeyboard'] = 'true'
            caps['automationName'] = 'uiautomator2'
            caps['settings[waitForIdleTimeout]']='10'
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(7)
        # 回到这个页面的目的是为了调用该也页面下的其他函数，如果不返回self则不能调用到goto_index这个函数
        return self

    def goto_index(self):
        """
        进入到首页
        :return:
        """
        return SearchOrder(self.driver)

    def app_quit(self):
        """
        关闭app
        :return:
        """
        self.driver.quit()
        time.sleep(5)
