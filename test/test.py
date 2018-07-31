#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh

from Person import Person
from ArithemeticSequence import ArithemeticSequence
from Fibs import Fibs
import sys, pprint

per1 = Person()
per1.set_name('shabi')
per1.greet()

s = ArithemeticSequence(start=3, step=5)
print(s[4])

fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break


def flatten(nested):
    """ 包含 yield 语句的函数都称为 生成器 """
    try:
        # 不迭代类似于字符串的对象
        try:
            # 尝试字符串拼接
            nested + ''
        except TypeError:
            # 不能拼接，说明不是字符串
            pass
        else:
            # 能拼接 是字符串 引发typeerror异常，外层except捕获typeerror异常，返回nested
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


nested = [[1, 2], [3, 4, 5], [6]]
for num in flatten(nested):
    print(num)
# 打印python搜索路径
# pprint.pprint(sys.path)
