#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:05:41 2020

@author: oleksiy
"""

givenFirstString = set(input("Enter firts string: "))
givenSecondString = set(input("Enter second string: "))
unitedSetOdStrings = sorted(set.union(givenFirstString,givenSecondString))

print(givenFirstString)
print(givenSecondString)
print(unitedSetOdStrings)

