# Author xuejie zeng
# encoding utf-8
from hogwarts.Homework_0816.api.wetag import WeTag

class TestWework:

    def test_creat(self):
        result =WeTag().test_create("yi", "001")["errmsg"]
        assert result == "created"

    def test_get(self):
        result = WeTag().test_get("001")["errmsg"]
        assert result == "ok"

    def test_updata(self):
        result = WeTag().test_get_update("001",'updateya1')["errmsg"]
        assert result == "updated"

    def test_delete(self):
        result =WeTag().test_delete("001")["errmsg"]
        assert result == "deleted"
