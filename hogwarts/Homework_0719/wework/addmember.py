# Author xuejie zeng
# encoding utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from hogwarts.Homework_0719.wework.base_page import Basepage


class AddMember(Basepage):

    def add_member(self):

        self.find(By.ID,'username').send_keys('zengxuejie')
        self.find(By.ID,'memberAdd_acctid').send_keys('zxj')
        self.find(By.ID,'memberAdd_phone').send_keys('16562898887')
        self.find(By.CSS_SELECTOR,".js_btn_save").click()




