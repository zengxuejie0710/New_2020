import yaml
from selenium.webdriver.common.by import By

from hogwarts.Homework_0805.page.base_page import BasePage
from hogwarts.Homework_0805.page.search import Search


class Market(BasePage):
    def goto_search(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        self.steps("../page/market.yaml", "goto_search")

        return Search(self.driver)