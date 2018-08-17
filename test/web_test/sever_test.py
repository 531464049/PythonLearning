#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh
""" 简单的服务器 """
'''
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
'''
'''
# 基于SocketServer的极简服务器
from socketserver import TCPServer, StreamRequestHandler


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('获取到来自 %s 的请求' % addr)
        self.wfile.write('89898989898989')


server = TCPServer(('', 1234), Handler)
server.serve_forever()
'''
'''
# 分叉服务器
from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler


class Server(ForkingMixIn, TCPServer):
    pass


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('获取到来自 %s 的请求' % addr)
        self.wfile.write('78787878')


server = Server(('', 1234), Handler)
server.serve_forever()
'''
'''
# 线程化服务器
from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler


class Server(ThreadingMixIn, TCPServer):
    pass


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('获取到来自 %s 的请求' % addr)
        self.wfile.write('78787878')


server = Server(('', 1234), Handler)
server.serve_forever()
'''
'''
# 使用select的简单服务器
import socket, select

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)
inputs = [s]
while True:
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r is s:
            c, addr = s.accept()
            print('获取到来自 %s 的请求' % addr)
            inputs.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True

            if disconnected:
                print(r.getpeername(), 'disconnected')
                inputs.remove(r)
            else:
                print(data)
'''
# 使用Twisted创建的简单服务器
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory


class SimpleLooger(Protocol):
    def connectionMade(self):
        print('获取到来自 %s  的请求' % self.transport.client)

    def connectionLost(self):
        print(self.transport.client, 'disconnected')

    def dataReceived(self, data):
        print(data)


factory = Factory()
factory.protocol = SimpleLooger

reactor.listenTCP(1234, factory)
reactor.run()