#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh


class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    size = property(get_size, set_size)

