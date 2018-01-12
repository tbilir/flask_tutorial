# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 11:33:52 2018

@author: tbilir
"""

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'