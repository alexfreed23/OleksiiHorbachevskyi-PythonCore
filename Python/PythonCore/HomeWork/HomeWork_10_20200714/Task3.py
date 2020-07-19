#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 20:55:36 2020

@author: oleksii
"""

noNneedExit = True
positive = 0
negative = 0

while noNneedExit:
    try:
        enteredNumber = int(input("Enter number: "))
        if enteredNumber == 0:
            noNneedExit = False
        #continue
        if enteredNumber < 0:
            negative += 1
        if enteredNumber > 0:
            positive += 1
    except ValueError:
        print("Unable to work with string ")
    try:
        print("Entered positive numbers in percents: ", round((positive / (positive + negative)) * 100), "%")
        print("Entered negative numbers in percents: ", round((negative / (positive + negative)) * 100), "%")
    except ZeroDivisionError:
        print("Zero is not working here :)")
