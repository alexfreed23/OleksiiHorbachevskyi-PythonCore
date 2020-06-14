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
    if (len(str(abs(int(value)))) == 1):
        numbersCount = "one-digit"
    elif len(str(abs(int(value)))) == 2:
        numbersCount = "two-digits"
    elif len(str(abs(int(value)))) == 3:
        numbersCount = "three-digits"
    elif len(str(abs(int(value)))) == 4:
        numbersCount = "four-digits"
    elif len(str(abs(int(value)))) == 5:
        numbersCount = "five-digits"
    elif len(str(abs(int(value)))) == 6:
        numbersCount = "six-digits"
    elif len(str(abs(int(value)))) == 7:
        numbersCount = "seven-digits"
    elif len(str(abs(int(value)))) == 8:
        numbersCount = "eight-digits"
    elif len(str(abs(int(value)))) == 9:
        numbersCount = "nine-digits"
    elif len(str(abs(int(value)))) == 10:
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
