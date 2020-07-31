# Author xuejie zeng
# encoding utf-8
# 1、使用参数化数据驱动，完成加减乘除测试用例的自动生成
# 2、修改测试用例为check_开头，修改测试用例的执行规则，执行所有check_开头和test_开头的测试用例
import pytest
import yaml
from hogwarts.Homework_0712.cal import Calculator



with open("testdata.yml",encoding='utf-8') as f:
    data = yaml.safe_load(f)
    #加法的数据
    adddata = data['add'].values()
    addids = data['add'].keys()
    #减法的数据
    subdata = data['sub'].values()
    subids = data['sub'].keys()
    #乘法的数据
    muldata = data['mul'].values()
    mulids = data['mul'].keys()
    #除法的数据
    divdata = data['div'].values()
    divids = data['div'].keys()


class Check_Calculator():

    def setup(self):
        self.cal = Calculator()

    @pytest.mark.parametrize('a,b,result', adddata, ids=addids)
    def check_add(self, a,b,result):
        assert result == self.cal.add(a,b)

    @pytest.mark.parametrize('a,b,result', subdata, ids=subids)
    def test_sub(self,a,b,result):
        t=self.cal.sub(a, b)
        #保留两位
        div=round(t,2)
        assert result == div

    @pytest.mark.parametrize('a,b,result', muldata, ids=mulids)
    def check_mul(self,a,b,result):
        assert result == self.cal.mul(a,b)

    @pytest.mark.parametrize('a,b,result', divdata, ids=divids)
    def test_div(self,a,b,result):
        try:
            assert result == self.cal.div(a,b)
        except :
            return "除数不能为0"

if __name__=="__main__":
    pytest.main(['-vs', 'check_one.py'])
