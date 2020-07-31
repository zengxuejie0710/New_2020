# Author xuejie zeng
# encoding utf-8
import re
a = '￥75'
b = '￥3 x 1人'
c = '￥78'

aa= a.split("￥")[1]
bb=b.split('￥')[1].split('x')[0]
cc= c.split("￥")[1]
dd= int(aa) + int(bb)
print(dd)
print(int(cc) == dd)

"""
从配置文件获取相关的app测试配置信息
"""
from appium import webdriver
# from config.config import *
from common.log import logger
import time
from common.base import Base


# 道路客运-壹行天下app 安卓
# @logger('开始从配置文件中获取测试相关的配置')
# def road_transport():
#     desired_caps = {
#                     'platformName': 'Android',
#                     'platformVersion': '10',
#                     'deviceName': 'b427c1d6',
#                     'noReset': True,
#                     'automationName': 'uiautomator2',
#                     # 'ANDROID_UIAUTOMATOR':'uiautomator2',
#                     'appPackage': 'io.dcloud.H5A6DF4A7',   # 测试环境
#                     'appActivity': 'io.dcloud.H5A6DF4A7.MainActivity',  # 生产环境
#                     # 'appActivity': 'io.dcloud.PandoraEntry',
#                     # 'chromeOptions': {'androidProcess': 'com.tencent.mm/.plugin.appbrand.ui.AppBrandUI2'},
#                     'androidDeviceReadyTimeout': 20,
#                     'recreateChromeDriverSessions': True,
#                     'unicodeKeyboard': True,
#                     'sessionOverride': True,
#                     'resetKeyboard': True}
#     return desired_caps



from appium import webdriver
# from config.config import *
from common.log import logger
import time
desired_caps = {
                'platformName': 'Android',
                'platformVersion': '10',
                'deviceName': 'b427c1d6',
                'noReset': True,
                'automationName': 'uiautomator2',
                # 'ANDROID_UIAUTOMATOR':'uiautomator2',
                'appPackage': 'io.dcloud.H5A6DF4A7',   # 测试环境
                'appActivity': 'io.dcloud.H5A6DF4A7.MainActivity',  # 生产环境
                # 'appActivity': 'io.dcloud.PandoraEntry',
                # 'chromeOptions': {'androidProcess': 'com.tencent.mm/.plugin.appbrand.ui.AppBrandUI2'},
                'androidDeviceReadyTimeout': 20,
                'recreateChromeDriverSessions': True,
                'unicodeKeyboard': True,
                'sessionOverride': True,
                'resetKeyboard': True}


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(7)
driver.find_element('xpath', '//android.widget.TextView[@text="汽车票查询"]').click()
time.sleep(5)
driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup").click()
time.sleep(5)

# a = driver.find_element("xpath","//android.widget.TextView[@text='￥75']").text
####我是票价#####
a = driver.find_element('xpath','//android.view.ViewGroup[2]/android.widget.TextView[2]').text
print('我是金额',a)
amount =a.split("￥")[1]
# print("查看页面", driver.context)
# driver.find_element("xpath","//android.widget.TextView[@text='立即支付']").click()

# b =driver.find_element("xpath","//android.widget.TextView[@text='￥3 x 1人']").text
# print('我是服务费',b)


# c = driver.find_element("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.TextView[2]").text
###我是服务费########
b = driver.find_element('xpath','//android.view.ViewGroup[5]/android.widget.TextView[2]').text
print("我是xpath",b)

serve =b.split('￥')[1].split('x')[0]


# d = driver.find_element("xpath","//android.widget.TextView[@text='￥78']").text
######我是总金额###
d = driver.find_element('xpath','//android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[2]').text
print("我是总金额",d)
