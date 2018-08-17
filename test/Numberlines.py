#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh

import fileinput


def add_lineNum(filePath):
    for line in fileinput.input(files=filePath):
        line = line.rstrip()
        # num = fileinput.lineno()
        print(line)


def main():
    # add_lineNum('README.md')
    pass


if __name__ == '__main__':
    main()