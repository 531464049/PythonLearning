#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh
""" 简单的服务器 """
import socket
s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)  #最大连接数
while True:
    c, addr = s.accept()
    print('获取到来自 %s 的连接' % addr)
    c.send(b'shit')
    c.close()