#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh
""" 数据库？？？、 """

import sqlite3

import os
print(os.getcwd())
print('sdsd')

def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'
    return float(value)

conn = sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute('''
    CREATE TABLE food (
        id TEXT PRIMARY KEY,
        desc TEXT,
        water FLOAT,
        kcal FLOAT,
        protein FLOAT,
        fat FLOAT,
        ash FLOAT,
        carbs FLOAT,
        fiber FLOAT,
        suger FLOAT
    )
''')
query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'
field_count = 10
with open('./test/DB_TEST/ABBREV.txt') as file:
    for line in file:
        try:
            line.decode('utf8')
            print('11')
            fields = line.split('^')
            vals = [convert(f) for f in fields[:field_count]]
            curs.execute(query, vals)
        except:
            pass


conn.commit()
conn.close()

