#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 19:33:07 2020

@author: oleksii
"""

import calculator

print(calculator.summ(10,5))
print(calculator.diff(30,5))
print(calculator.product(2,5))
print(calculator.fraction(25,5))
print("-"*10)

from calculator import summ,diff
print(summ(5,5))
print(diff(5,5))
print("-"*10)


from calculator import summ,diff,product,fraction
# or
#from calculator import *

print(summ(5,5))
print(diff(5,5))
print(product(5,5))
print(fraction(5,5))
print("-"*10)
