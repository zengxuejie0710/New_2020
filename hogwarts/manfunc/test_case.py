# Author xuejie zeng
# encoding utf-8
import yaml

with open("data.yml",encoding='utf-8') as f :
    data = yaml.safe_load(f)
    datas = data.values()
    ids = data.keys()

def testcase(param):

    print(f"测试数据:{param}")
