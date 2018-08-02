#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh

""" 文件 """

import os
import sys

def readWordCount():
    text = sys.stdin.read()
    words = text.split()
    wordCount = len(words)
    print('单词数量:',wordCount)

def main():
    # 当前路径
    print(os.getcwd())
    pass

if __name__ == '__main__':
    main()