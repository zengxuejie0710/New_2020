# Author xuejie zeng
# encoding utf-8

# 1、实现添加联系人和删除联系人功能的代码
#
# 编写添加联系人测试用例
# 编写删除联系人测试用例
# 编码代码的时候注意点：
#
# 1、添加联系人页面动态的查找【添加成员】按钮
# 学习滚动查找页面元素
# 2、定位方式
# 学习多种定位方式的灵活运用
# 3、断言
# 验证页面的正确性
# 4、加分项：
# 使用 setup_class,teardown_class 初始化，使用setup,teardown 完成测试用例之间的切换
# 使用有规律的联系人名称，例如【霍格沃兹_1】，方便删除联系人
# 实现allure 测试报告生成

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWework():
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "5eb2803"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] =".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["platformVersion"] = "7.1.1"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def test_cont(self):

        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH,".//android.widget.TextView[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='从微信/手机通讯录中添加']").click()
        #滚动查找要添加的用户
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable'
                                 '(new UiSelector().'
                                 'scrollable(true).'
                                 'instance(0)).'
                                 'scrollIntoView('
                                 'new UiSelector().'
                                 'text("Axj").instance(0));')

        self.driver.find_element(MobileBy.XPATH,"//*[@text='Axj']/../../../*[@text='添加']").click()
