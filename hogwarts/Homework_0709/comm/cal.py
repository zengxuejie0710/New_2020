#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Calculator():

    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        try:
            chu=a/b
        except:
            return "除数不能为零"

