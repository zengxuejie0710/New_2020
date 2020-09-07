# coding:utf-8


from common.base import Base
from appium import webdriver
from page.order import SearchOrder
import pytest
import time
import os
import logging
import allure
#获取当前路径
cur_path = os.path.dirname(os.path.realpath(__file__))
#进入到report路径
error_img = os.path.join(os.path.dirname(cur_path),'report')


class App(Base):
    """
    壹行天下app配置
    :return:
    """

    def startapp(self):
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

    def stop(self):
        """
        关闭app
        :return:
        """
        self.driver.quit()


    def goto_index(self):
        """
        进入到首页
        :return:
        """
        return SearchOrder(self.driver)

    def save_scree_image(self):
        """
        对当前页面进行截图
        :return:
        """
        # start_time = time.time()
        start_time = time.strftime("%Y%m%d.%H.%M.%S")
        filename = '{}.png'.format(start_time)
        file_path = os.path.join(error_img, filename)
        self.driver.save_screenshot(file_path)
        logging.info("错误页面截图成功，图表保存的路径:{}".format(file_path))
        return file_path

    def save_image_to_allure(self):
        """
        保存失败的截图到allure报告中
        :return:
        """
        file_path = self.save_scree_image()
        with open(file_path, "rb") as f:
            file = f.read()
            allure.attach(file, "失败截图", allure.attachment_type.PNG)
