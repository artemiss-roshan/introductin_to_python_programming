# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 23:54:40 2021

@author: ASUS
"""

import os
os.system('cls')

def FindGcd(a, b):
    dividers = [1]
    for i in range(2, min(abs(a), abs(b))+1):
        if (a%i==0) & (b%i==0):
            dividers.append(i)
    return max(dividers)


def Sim(t):
    gcd = FindGcd(t[0], t[1])
    return (t[0]/gcd, t[1]/gcd)



# یک لیست از اعداد کسری میگیرد و آن اعداد را ساده میکند
def SimList(tNumbers):
    result = []
    for t in tNumbers:
        result.append(Sim(t))
    return result
