# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 23:53:19 2021

@author: ASUS
"""

def func3(num):
    count = 1
    cutnum = 0
    while num > count:
        count = count * 10
    while num > 1:
        while num > count:  
            cutnum += count          
            num=num- count
        count = count // 10
    return cutnum