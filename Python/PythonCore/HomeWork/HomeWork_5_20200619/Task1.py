#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:39:53 2020

@author: oleksiy
"""
import string

enteredText = input("Enter your text: ")
newLine = ""
i = 1
newLetter = 97
for letter in enteredText:
    if i == 4:
        if letter in string.ascii_letters:
            print(letter)
            letter = chr(newLetter)
            newLetter += 1
        i = 0
    newLine += letter
    i += 1
print(newLine)
