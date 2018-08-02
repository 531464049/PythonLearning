#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh
""" 图形用户界面 """
from tkinter import *
from tkinter.scrolledtext import ScrolledText


def load():
    name = fileName.get()
    if not name.strip():
        print('文件路径为空.....')
        return
    with open(name) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())


def save():
    with open(fileName.get(), 'w') as file:
        file.write(contents.get('1.0', END))


window = Tk()
window.title('shit')

contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)

fileName = Entry()
fileName.pack(side=BOTTOM, expand=True, fill=X)

btn1 = Button()
btn1.config(text='open', command=load)
btn1.pack(side=LEFT)

btn2 = Button()
btn2.config(text='save', command=save)
btn2.pack(side=LEFT)

mainloop()
