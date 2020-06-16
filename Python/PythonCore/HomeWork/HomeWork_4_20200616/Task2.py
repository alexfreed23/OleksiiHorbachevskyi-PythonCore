#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:03:33 2020

@author: oleksiy
"""
i = 1
numCanDivideOn5 = 0

while i <= 10:
    enteredNumber = int(input("Entet number greater than 2: "))
    if enteredNumber % 5 == 0:
        numCanDivideOn5 += 1
    i += 1
print(numCanDivideOn5," number(s) can be devided on 5")
