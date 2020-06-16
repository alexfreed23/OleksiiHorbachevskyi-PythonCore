#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:05:31 2020

@author: oleksiy
"""

noNneedExit = True
positive = 0
negative = 0

while noNneedExit:
    enteredNumber = int(input("Enter number: "))
    if enteredNumber == 0:
        noNneedExit = False
        #continue
    if enteredNumber < 0:
        negative += 1
    if enteredNumber > 0:
        positive += 1
print("Entered positive numbers in percents: ", round((positive / (positive + negative)) * 100), "%")
print("Entered negative numbers in percents: ", round((negative / (positive + negative)) * 100), "%")
