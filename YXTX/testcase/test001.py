# encoding utf-8
from common.config import App
import pytest
import yaml
import os
import allure

def get_root_dir():
    return os.path.dirname(os.path.dirname(__file__))

with open(get_root_dir() + '/datas/yxtx_data.yaml', encoding="utf-8")as f:
    testdata = yaml.safe_load(f)


@allure.feature("YXTX测试用例")
class TestSearchReservation:
    def setup(self):
        print('* * * Start * * *')
        self.app = App().startapp()

    def teardown(self):
        print('* * * End * * *')
        self.app.stop()
        self.app.stop()

    @allure.story("始发站-到达站")
    @pytest.mark.parametrize("start,end",testdata)
    def test01(self,start,end,):
        """
        用例描述：
        用例步骤：
            1.进入app首页
            2.判断是否存在未支付的订单
            3.输入出发站和到达站地址
            4.获取页面地址,金额
            5.点击立即支付按钮
            6.看订单信息内容
            7.获取乘车地址,电话,取消订单
        :param start:
        :param end:
        :return:
        """
        try:

            with allure.step("进入app首页"):
                first_step = self.app.goto_index()
            with allure.step("判断是否存在未支付的订单"):
                first_step.isexit_order()
            with allure.step("输入出发站和到达站地址"):
                first_step.deparstaion(start, end)
            with allure.step("获取页面地址,金额"):
                origin_stop = first_step.verity_start()
                arrival_stop = first_step.verity_end()
                amount, serve = first_step.getsum()
            with allure.step("点击立即支付按钮"):
                first_step.now_pay()
            with allure.step("看订单信息内容"):
                first_step.order_context()
            with allure.step("获取乘车地址,电话,取消订单"):
                adress = first_step.is_adress()
                phone = first_step.is_phone()
                result = first_step.cancal_order()
            assert (origin_stop)
            assert (arrival_stop)
            assert (amount != serve)
            assert (adress)
            assert (phone)
            assert (result)

        except Exception as msg:
            print(u"异常原因%s" % msg)
            self.app.save_image_to_allure()
            raise



