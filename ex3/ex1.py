# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 23:50:40 2021

@author: ASUS
"""

import os
os.system('cls')

#یک جمله را به کلماتش تقسیم میکند
def SplitSent(sentence): 
    return sentence.split(' ')


print(SplitSent("hello how are you?"))