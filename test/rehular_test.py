#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh
""" 正则表达式 """

import re

# 通配符 . 句点与除换行符外的其他字符都匹配只,与一个字符匹配，而不与零或两个字符匹配
# r1 = '.ython'

# 转义 \ 使用原始字符串
# r'python\.org'

# 字符集 字符集只能匹配一个字符
# '[a-z]' 与a~z的任何字母都匹 配
# '[a-zA-Z0-9]' 与大写字母、小写字母和 数字都匹配
# '[^abc]' 排除字符集 与除a、b和c外的其他任何字符 都匹配
'''
some_text = "aklkl, kjdghh ,,, hjduyghuy  , sdbgu     def"
result = re.split('[, ]+', some_text)
print(result)

pat = '[a-zA-Z]+'
test = '"haha" ... njdhfj ndjkghdfj  sdfgjhh a sdfbn jdf a./,/sf bfn bjjh slkhv'
print(re.findall(pat, test))

pat = '{name}'
text = 'dear {name} ...'
print(re.sub(pat, 'shabi', text))

pat = r'www\.(.*)\..{3}'
m = re.match(pat, 'www.python.org')
print(m.group(1))
print(m.start(1))
print(m.end(1))
print(m.span(1))

emphasis_patten = r'\*([^\*]+)\*'
newText = 'hello, *nihao*!'
htmlText = re.sub(emphasis_patten, r'<em>\1<em>', newText)
print(htmlText)
'''
import fileinput
import os
def find_email_from(path):
    """ 匹配邮件内容 找出发件人 """
    pat = re.compile('From: (.*) <.*?>$')
    for line in fileinput.input(files=path):
        m = pat.match(line)
        if m:
            print('发件人：',m.group(1))


def main():
    print(os.getcwd()) #当前路径
    find_email_from(path='./test/email_text.text')

if __name__ == '__main__':
    main()