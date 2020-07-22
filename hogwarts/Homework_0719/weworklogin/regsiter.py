# Author xuejie zeng
# encoding utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Regsiter():
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def regsiter(self):
        '''
        企业注册信息
        :return:
        '''
        self.driver.find_element(By.ID,'corp_name').send_keys("zengxuejie")
        self.driver.find_element(By.ID,'manager_name').send_keys('zxj')
        self.driver.find_element(By.ID,'register_tel').send_keys('15652876666')

        return True

