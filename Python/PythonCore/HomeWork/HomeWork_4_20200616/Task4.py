#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:37:18 2020

@author: oleksiy
"""

firstLastLine = "+------------------------------------------------------------------+"
middlePartOfRect = "|******************************************************************|"

a = 0
b = 10

for i in range(a,b):
    if i == a or i == b - 1:
        print(firstLastLine)
    else:
        print(middlePartOfRect)
