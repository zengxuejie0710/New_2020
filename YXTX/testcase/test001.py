# encoding utf-8
from YXTX.common.config import App
import pytest
import yaml

with open("../datas/yxtx_data.yaml", encoding="utf-8")as f:
    testdata = yaml.safe_load(f)

class TestSearchReservation:

    def setup(self):
        print('* * * Start * * *')
        self.app = App()
    def tearDown(self):
        print('* * * End * * *')
        self.app.app_quit()

    @pytest.mark.parametrize("start,end",testdata)
    def test01(self,start,end):
        first_step = self.app.start().goto_index()
        first_step.isexit_order()
        first_step.deparstaion(start, end)
        origin_stop = first_step.verity_start()
        arrival_stop = first_step.verity_end()
        amount, serve = first_step.getsum()
        first_step.now_pay()
        first_step.order_context()
        adress = first_step.is_adress()
        phone = first_step.is_phone()
        result = first_step.cancal_order()
        assert (origin_stop)
        assert (arrival_stop)
        assert (amount == serve)
        assert (adress)
        assert (phone)
        assert (result)