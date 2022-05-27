# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:23:33 2022

@author: dwand
"""

def sq(func,x):
    y = x**2
    return func(y)

def f(x):
    return x**2

calc = sq(f,2)
print(calc)
