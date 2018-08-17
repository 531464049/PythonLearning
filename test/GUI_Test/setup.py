#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh

# from setuptools import setup

# setup(
#     name='hello',
#     version='1.0',
#     description='simple simple',
#     author='mh',
#     py_modules=['tkinter_test'])


from distutils.core import setup
import py2exe

setup(console=['tkinter_test.py'])