#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh

import sys,shelve

def store_person(db):
    """ 将输入内容存储到shelf对象中 """
    pid = input('输入id：')
    person = {}
    person['name'] = input('输入名字：')
    person['age'] = input('输入age：')
    person['phone'] = input('电话：')
    db[pid] = person

def lookup_person(db):
    """ 根据id读取shelf对象对应的数据 """
    pid = input('要查询的id：')
    print('读取的内容:',db[pid])

def printHelp():
    print('The available commands are:')
    print('store : Stores information about a person')
    print('lookup : Looks up a person from ID number')
    print('quit : Save changes and exit')
    print('? : Prints this message')

def enter_command():
    cmd = input('输入：（？）：')
    cmd = cmd.strip().lower()
    return cmd

def main():
    db = shelve.open('./test/testdb')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(db)
            elif cmd == 'lookup':
                lookup_person(db)
            elif cmd == '?':
                printHelp()
            elif cmd == 'quit':
                return
    finally:
        db.close()

if __name__ == '__main__':
    main()