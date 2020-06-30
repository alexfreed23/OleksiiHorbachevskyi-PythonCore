#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 00:17:02 2020

@author: oleksiy
"""

enteredString = input("Please enter string: ")
stringToDictionary = list(enteredString.replace("  ", " ").split(" "))
listToDict = {}
for element in stringToDictionary:
    listToDict[element] = stringToDictionary.count(element)
print(listToDict)
