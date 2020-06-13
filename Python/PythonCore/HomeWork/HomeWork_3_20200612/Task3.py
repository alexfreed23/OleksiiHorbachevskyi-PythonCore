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
    if (len(value) == 1) and (positiveOrNegative == "pozitive"):
        numbersCount = "one-digit"
    elif len(value) == 2 and (positiveOrNegative == "pozitive") :
        numbersCount = "two-digits"
    elif len(value) == 3 and (positiveOrNegative == "pozitive"):
        numbersCount = "three-digits"
    elif len(value) == 4 and (positiveOrNegative == "pozitive"):
        numbersCount = "four-digits"
    elif len(value) == 5 and (positiveOrNegative == "pozitive"):
        numbersCount = "five-digits"
    elif len(value) == 6 and (positiveOrNegative == "pozitive"):
        numbersCount = "six-digits"
    elif len(value) == 7 and (positiveOrNegative == "pozitive"):
        numbersCount = "seven-digits"
    elif len(value) == 8 and (positiveOrNegative == "pozitive"):
        numbersCount = "eight-digits"
    elif len(value) == 9 and (positiveOrNegative == "pozitive"):
        numbersCount = "nine-digits"
    elif len(value) == 10 and (positiveOrNegative == "pozitive"):
        numbersCount = "ten-digits"
    elif ((len(value) - 1) == 1) and (positiveOrNegative == "negative"):
        numbersCount = "one-digit"
    elif (len(value) - 1 == 2) and (positiveOrNegative == "negative") :
        numbersCount = "two-digits"
    elif (len(value) - 1 == 3) and (positiveOrNegative == "negative"):
        numbersCount = "three-digits"
    elif (len(value) - 1 == 4) and (positiveOrNegative == "negative"):
        numbersCount = "four-digits"
    elif (len(value) - 1 == 5) and (positiveOrNegative == "negative"):
        numbersCount = "five-digits"
    elif (len(value) - 1 == 6) and (positiveOrNegative == "negative"):
        numbersCount = "six-digits"
    elif (len(value) - 1 == 7) and (positiveOrNegative == "negative"):
        numbersCount = "seven-digits"
    elif (len(value) - 1 == 8) and (positiveOrNegative == "negative"):
        numbersCount = "eight-digits"
    elif (len(value) - 1 == 9) and (positiveOrNegative == "negative"):
        numbersCount = "nine-digits"
    elif (len(value) - 1 == 10) and (positiveOrNegative == "negative"):
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


