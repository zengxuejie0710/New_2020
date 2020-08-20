# Author xuejie zeng
# encoding utf-8
import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from hogwarts.Homework_0730.basepage.handlerblack import handle_black

_black_list = [
    (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")
]
_max_err_num = 3
_error_num = 0

class Base():

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_black
    def find(self, by, locator=None):
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    # def finds(self,locator):
    #     logging.info(f'find: {locator}')
    #     elements = WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_elements(*locator))
    #     return elements
    def finds(self,by,locator=None):
        if locator is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, locator)

    def set_implicitly_wait(self, second):
        self.driver.implicitly_wait(second)


    def click_element(self,locator):
        logging.info(f'find:{locator}')
        self.find(locator).click()


    def find_and_sendkeys(self,locator,text):
        logging.info(f'find:{locator},text:{text}')
        self.find(locator).send_keys(text)


    def find_by_scroll(self, text):
        logging.info('find_by_scroll')
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));')


    def webdriver_wait(self, locator, timeout=20):
        logging.info(f'webdriver_wait: {locator}, timeout: {timeout}')
        element = WebDriverWait(self.driver, timeout).until(
            lambda x: x.find_element(*locator))
        return element


    def back(self, num=1):
        logging.info(f'back: {num}')
        for i in range(num):
            self.driver.back()