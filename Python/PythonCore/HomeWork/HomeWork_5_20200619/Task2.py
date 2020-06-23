#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:26:26 2020

@author: oleksiy
"""

import string

enteredText = input("Enter your text: ")
newLine = ""
i = 1
for letter in enteredText:
    if (i == 4) and (letter in string.ascii_letters):
        newLetter = ord(letter) - 3
        print(newLetter)
        if newLetter == 96:
            newLetter = 122
            print(newLetter)
            newLine += chr(newLetter)
        elif newLetter == 95:
            newLetter = 121
            print(newLetter)
            newLine += chr(newLetter)
        elif newLetter == 94:
            newLetter = 120
            print(newLetter)
            newLine += chr(newLetter)
        print(letter, "replaced with ", chr(newLetter))
        i = 0
    else:
        newLine += letter
    i += 1
print(newLine)
