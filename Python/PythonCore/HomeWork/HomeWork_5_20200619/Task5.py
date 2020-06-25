#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 19:19:00 2020

@author: oleksiy
"""

enteredText = input("Enter text: ")

isUpperCase = False
isLowerCase = False

for letter in enteredText:
    if ord(letter) in range(97,123):
        isLowerCase = True
    if ord(letter) in range(65,91):
        isUpperCase = True
if isUpperCase:
    print("Text contain UPPERCASE letter")
else:
    print("Text does not contain UPPERCASE letter")
    
if isLowerCase:
    print("Text contain lowercase letter")
else:
    print("Text does not contain lowercase letter")
    
