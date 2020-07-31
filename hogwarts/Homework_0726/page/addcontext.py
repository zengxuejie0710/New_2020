# Author xuejie zeng
# encoding utf-8


from appium.webdriver.common.mobileby import MobileBy
from hogwarts.Homework_0726.basepage.base import Base


class AddContext(Base):
    name =(MobileBy.XPATH,"//*[contains(@text, '姓名')]/../*[@class='android.widget.EditText']")
    sex = (MobileBy.XPATH,"//*[@text='性别']/../*[@resource-id='com.tencent.wework:id/e93']")
    male =(MobileBy.XPATH,"//*[@text='男']")
    phone=(MobileBy.XPATH,"//*[@text='手机号']")
    save =(MobileBy.ID,"com.tencent.wework:id/hi9")

    def set_name(self,filename):
        """
        设置名字
        :return:
        """
        # self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys('联系')

        self.find_and_sendkeys(self.name,filename)
        return self
    def set_sex(self):
        """
        设置性别
        :return:
        """
        self.click_element(self.sex)
        self.click_element(self.male)
        return self
    def set_phone(self,phonenum):
        """
        设置手机号
        :return:
        """
        self.find_and_sendkeys(self.phone,phonenum)
        return self
    def click_save(self):
        """
        点击保存
        :return:
        """
        self.click_element(self.save)
        from hogwarts.Homework_0726.page.addmember import Add_Input
        return Add_Input(self.driver)

