# Author xuejie zeng
# encoding utf-8
# 1、使用参数化数据驱动，完成加减乘除测试用例的自动生成
# 2、修改测试用例为check_开头，修改测试用例的执行规则，执行所有check_开头和test_开头的测试用例
import pytest
import yaml
from hogwarts.casedriver.cal import Calculator


with open("testdata.yml") as f:
    data = yaml.safe_load(f)
    #加法的数据
    adddata = data.values()
    addids = data.keys()
    print("------",adddata,addids)

def get_step():

    with open("steps/casedata.yml")as f:
        datas = yaml.safe_load(f)
    return  datas

cal = Calculator()

def step(a,b,result):
    step1=get_step()
    for i in step1:
        print('i的值是：', i)
        if 'add' == i:
            t = cal.add(a, b)
            print('t的值是',result)
            r=result
            print("r的值是",r)
            assert r == t
        elif 'add1' == i:
            assert result == cal.add1(a, b)
        elif 'add2' == i:
            assert result == cal.add2(a, b)



class Test_Calculator():
    @pytest.mark.parametrize('a,b,result', adddata, ids=addids)
    def test_add(self, a,b,result):
        print('a,b,c的值',a,b,result)
        step(a,b,result)


if __name__=="__main__":
    pytest.main(['-vs', 'test_add.py'])
