# Author xuejie zeng
# encoding utf-8

import pytest
import yaml
from hogwarts.Homework_0712.cal import Calculator


# 控制测试用例顺序按照【加-减-乘-除】这个顺序执行,
# 减法依赖加法， 除法依赖乘法

@pytest.mark.parametrize('a,b',[(1,2),(3,4)])
class Test_Calculator():
    def setup(self):
        self.cal = Calculator()

    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name="a")
    def test_add(self, a,b):
        print("a+b",a+b)
        result=a+b
        assert result == self.cal.add(a,b)

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(name="s",depends=["a"])
    def test_sub(self,a,b):
        print("a+b",a-b)
        result=a-b
        assert result == self.cal.sub(a,b)

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(name="d",depends=["m"])
    def test_div(self,a,b):
        try:
            result = a / b
            assert result == self.cal.div(a,b)
        except :
            return "除数不能为0"

    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name="m")
    def test_mul(self,a,b):

        print("a+b",a * b)
        result=a * b
        assert result == self.cal.mul(a,b)

if __name__=="__main__":
    pytest.main(['-vs', 'check_two.py'])

