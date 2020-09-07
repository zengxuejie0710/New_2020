# encoding utf-8
from common.config import App
import pytest
import yaml
import os
import allure

def get_root_dir():
    return os.path.dirname(os.path.dirname(__file__))
print(get_root_dir())

with open(get_root_dir() + '/datas/yxtx_data.yaml', encoding="utf-8")as f:
    testdata = yaml.safe_load(f)

class TestSearchReservation:

    def setup(self):
        print('* * * Start * * *')
        self.app = App().startapp()

    def teardown(self):
        print('* * * End * * *')
        self.app.stop()


    @pytest.mark.parametrize("start,end",testdata)
    def test01(self,start,end,):
        try:

            with allure.step("进入首页"):
                first_step = self.app.goto_index()
            with allure.step("判断是否存在未支付的订单"):
                first_step.isexit_order()
            first_step.deparstaion(start, end)
            origin_stop = first_step.verity_start()
            arrival_stop = first_step.verity_end()
            amount, serve = first_step.getsum()
            # first_step.now_pay()
            # first_step.order_context()
            # adress = first_step.is_adress()
            # phone = first_step.is_phone()
            # result = first_step.cancal_order()
            # assert (origin_stop)
            # assert (arrival_stop)
            assert (amount != serve)
            # assert (adress)
            # assert (phone)
            # assert (result)
        except:
            self.app.save_image_to_allure()



