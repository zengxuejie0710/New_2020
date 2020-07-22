# Author xuejie zeng
# encoding utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from hogwarts.Homework_0719.wework.addmember import AddMember
from hogwarts.Homework_0719.wework.base_page import Basepage


class IndexOne(Basepage):

    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_member(self):
        '''
        点击添加成员
        :return:
        '''
        def add_member_con(x):
            elements = len(self.finds(By.ID,'username'))
            if elements <= 0 :
                self.find(By.XPATH,"//*[@class='js_has_member']//*[@class='qui_btn ww_btn js_add_member']").click()
                #css方式
                #self.find(By.XPATH,'.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
            return elements > 0

        self.find(By.ID,'menu_contacts').click()
        sleep(2)
        self.wait_for_condition(add_member_con)
        return AddMember(self._driver)


    def import_member(self):
         '''
         导入通讯录
         :return:
         '''
         pass

    def join_member(self):
         '''
         成员加入
         :return:
         '''
         pass
