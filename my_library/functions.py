#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:10:16 2020

@author: yujiang
"""
import datetime

def hello_world(param=2):
    """
    this is to test how to use sphinx.ext.autodoc
    
    :param var: (int) just a test a param (default is 2)
    :param datetime: (int) just a test param (default is 1)
    :return: (str) hello world time str
    """
    today = datetime.date.today()
    to_string =  "hello world to {} in {}".format(param, today)
    print(to_string)
    return to_string 
