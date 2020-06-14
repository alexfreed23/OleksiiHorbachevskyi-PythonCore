#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:50:39 2020

@author: oleksiy

Task 3
"""
value = input("Please enter a number: \n")
try:
    if int(value) < 0:
        positiveOrNegative = "negative"
    elif int(value) > 0:
        positiveOrNegative = "pozitive"
    else:
        positiveOrNegative = "zero"
    
    valueLength = len(str(abs(int(value))))
    
    if valueLength == 1:
        numbersCount = "one-digit"
    elif valueLength == 2:
        numbersCount = "two-digits"
    elif valueLength == 3:
        numbersCount = "three-digits"
    elif valueLength == 4:
        numbersCount = "four-digits"
    elif valueLength == 5:
        numbersCount = "five-digits"
    elif valueLength == 6:
        numbersCount = "six-digits"
    elif valueLength == 7:
        numbersCount = "seven-digits"
    elif valueLength == 8:
        numbersCount = "eight-digits"
    elif valueLength == 9:
        numbersCount = "nine-digits"
    elif valueLength == 10:
        numbersCount = "ten-digits"
    else:
        numbersCount=str(len(str(abs(int(value))))) + " digits"
        if int(value) < 0:
            positiveOrNegative = "negative"
        elif int(value) > 0:
            positiveOrNegative = "pozitive"
    print(positiveOrNegative, numbersCount)
except ValueError:
    print("That's not a number")
