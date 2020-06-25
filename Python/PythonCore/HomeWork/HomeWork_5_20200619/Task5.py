#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 19:19:00 2020

@author: oleksiy
"""

enteredText = input("Enter text: ")
resultText = ""
for letter in enteredText:
    if ord(letter) == 32:
        resultText = resultText + "_"
    else:
        resultText = resultText + letter
print(resultText)
    
