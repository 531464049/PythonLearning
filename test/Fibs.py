#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh


class Fibs:
    """ 实现了方法__iter__的对象是可迭代的，
    而实现了方法__next__的对象 是迭代器。
    """
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self

def main():
    pass

if __name__ == '__main__':
    main()