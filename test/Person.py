#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh


class Person(object):
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print('peoson 名字: {}', format(self.name))
