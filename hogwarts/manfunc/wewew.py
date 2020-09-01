# Author xuejie zeng
# encoding utf-8
import re

#a = "安龙(-------)"
a= '安龙 (ooo)'

if "("in a:
    print('1111')
#print(re.findall(r'[(](.*?)[)]', a))
    p1 = re.compile(r'[(](.*?)[)]', re.S)
    arr = re.findall(p1, a)[0]
    print(arr)

    if '--'in arr:
        print("正确")
    else:
        print('ddd')

# print(float(105))
# a = float(10)
# b = float(20)
#
# print(a+b)
