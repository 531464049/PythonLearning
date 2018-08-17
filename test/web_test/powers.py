#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh

from flask import Flask

app = Flask(__name__)


@app.route('/')
def powers(n=10):
    return ','.join(str(2**i) for i in range(n))


app.run(host='0.0.0.0')
