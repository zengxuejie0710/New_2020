# Author xuejie zeng
# encoding utf-8

class Calculator():

    def add(self,a,b):
        print('a+b=',a+b)
        return a+b

    def add1(self,a,b):
        print('a+b=',a+b)
        return a+b

    def add2(self,a,b):
        print('a+b=',a+b)
        return a+b


    def div(self,a,b):
        try:
            chu=a/b
        except:
            return "除数不能为零"