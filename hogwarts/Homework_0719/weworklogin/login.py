# Author xuejie zeng
# encoding utf-8

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from hogwarts.Homework_0719.weworklogin.regsiter import Regsiter


class TestLogin():
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def scan_login(self):
        """
        扫码登录
        :return:
        """
        pass
    def goto_regsiter(self):
        """
        点击企业登录
        进入到登录页面
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,'.login_registerBar_link').click()
        return Regsiter(self.driver)
