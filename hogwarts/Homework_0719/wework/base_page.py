# Author xuejie zeng
# encoding utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class Basepage:
    _driver = None
    _base_url = ''

    def __init__(self,driver:WebDriver=None):

        if self._driver == None:
            chromenew = Options()
            chromenew.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=chromenew)
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver

        if self._base_url != '':
            self._driver.get(self._base_url)


    def find(self,by,locator):
        return self._driver.find_element(by,locator)

    def finds(self,by,locator):
        return self._driver.find_elements(by,locator)

    def wait_for_condition(self,condition):
        WebDriverWait(self._driver,10).until(condition)


