#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh

import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))
print(s.recv(1024))