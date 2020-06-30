#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:37:10 2020

@author: oleksiy
"""
import string

givenString = input("Enter string: ")
#givenStringAsList = list(givenString.split(" "))
resultString = ""
rememberedChar = ""
for element in givenString:
    if element not in string.ascii_letters:
        if rememberedChar == element:
            continue
        else:
            rememberedChar = element
    resultString +=  element
print(resultString)

