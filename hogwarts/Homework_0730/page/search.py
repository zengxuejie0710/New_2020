# Author xuejie zeng
# encoding utf-8
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from hogwarts.Homework_0730.basepage.base import Base


class SearchPage(Base):
    input_data = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']")
    click_ali = (By.XPATH, "//*[@text='阿里巴巴-SW' and @resource-id='com.xueqiu.android:id/name']")


    def search(self):
        self.find_and_sendkeys(self.input_data,"阿里巴巴")
        self.click_element(self.click_ali)
        self.driver.find_element_by_xpath(
                  "//*[contains(@resource-id, 'stock_item_container')]//*[@text='阿里巴巴']/../..//*[@text='加自选']").click()


    def is_choose(self, stock_name):
        eles = self.driver.find_element_by_xpath("//*[contains(@resource-id, 'stock_item_container')]//*[@text='阿里巴巴']/../..//*[@text='已添加']")
        return len(eles) > 0