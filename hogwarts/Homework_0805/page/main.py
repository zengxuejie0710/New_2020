import yaml
from selenium.webdriver.common.by import By

from hogwarts.Homework_0805.page.base_page import BasePage
from hogwarts.Homework_0805.page.market import Market


class Main(BasePage):

    def goto_market(self):
        # 伪造黑名单
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        self.set_implicitly_wait(7)
        self.steps("../page/main.yaml", "goto_market")
        return Market(self.driver)
