# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:54:48 2018

@author: tbilir
"""

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes