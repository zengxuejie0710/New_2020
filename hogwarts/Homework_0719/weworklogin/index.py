# Author xuejie zeng
# encoding utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

from hogwarts.Homework_0719.weworklogin.login import TestLogin
from hogwarts.Homework_0719.weworklogin.regsiter import Regsiter


class Index():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')

    def goto_register(self):
        """
        点击企业注册
        进入到注册的页面
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return Regsiter(self.driver)

    def goto_login(self):
        """
        点击企业登录
        进入到登录页面
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return TestLogin(self.driver)
