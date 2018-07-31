#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh


def check_index(key):
    """ 指定的键是否是可接受的索引?
        键必须是非负整数，才是可接受的。如果不是整数，
        将引发TypeError异常;如果是负数，
        将引发Index Error异常(因为这个序列的长度是无穷的)
    """
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithemeticSequence(object):
    def __init__(self, start=0, step=1):
        """ 初始化这个序列
        start -序列中的第一个值
        step -两个相邻值的差
        changed -一个字典，包含用户修改后的值
        """
        self.start = start  # 存储起始值
        self.step = step  # 存储步长
        self.changed = {}  # 没有任何元素被修改

    def __getitem__(self, key):
        """ 从序列中获取一个元素 """
        check_index(key)
        try:
            # 修改过，直接返回修改后的值
            return self.changed[key]
        except KeyError as error:
            print(error)
            # 没有修改过，返回计算后的值
            return self.start + key * self.step

    def __setitem__(self, key, value):
        """ set 修改序列中的元素 """
        check_index(key)
        # 存储要修改的值
        self.changed[key] = value