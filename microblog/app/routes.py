# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 17:06:27 2018

@author: tbilir
"""

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"