#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh

from Person import Person

squares = {i: '{} squeres is {}'.format(i, i**2) for i in range(10)}
print(squares)

# 使用 exec 和 eval 执行字符串及计算结果
exec('print("jkjkjkjk")')


def story(**kw):
    print('once upon a time,there was a'\
        '{job} called {name}.'.format_map(kw))


def power(x, y, *others):
    if others:
        print('获取到更多参数：', others)
    print('pow:', pow(x, y))


def interval(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    result = []

    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

per1 = Person()
per1.set_name('shabi')
per1.greet()