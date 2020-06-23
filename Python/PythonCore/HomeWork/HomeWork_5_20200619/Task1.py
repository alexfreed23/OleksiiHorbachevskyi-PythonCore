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
for letter in enteredText:
    if (i == 4) and (letter in string.ascii_letters):
        newLetter = ord(letter) + 4
        if newLetter >= 123:
            newLetter = 96 + (newLetter - 123)
            newLine += chr(newLetter)
        elif newLetter >= 90 and newLetter < 97:
            newLetter = 64 + (newLetter - 90)
            newLine += chr(newLetter)
        print(letter, "replaced to ", chr(newLetter))
        i = 0
    newLine += letter
    i += 1
print(newLine)