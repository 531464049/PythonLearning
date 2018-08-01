#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh
""" 时间 time random 随机数 """

import time
import random

# 当前时间 时间戳
print(time.time())
# 当前时间 字符串
print(time.asctime())

date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = time.mktime(date1)
date2 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = time.mktime(date2)
print(time1, time2)
# 随机一个time1-time2的随机数（不包括time2）
random_time = random.uniform(time1, time2)
print(time.asctime(time.localtime(random_time)))