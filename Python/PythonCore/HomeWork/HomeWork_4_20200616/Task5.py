#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:43:03 2020

@author: oleksiy
"""
P = int(input("Enter number P: "))
H = int(input("Enter number H: "))

noNneedExit = True
sumEnteredIfLessP = 0
productOgNumMoreH = 1
countNumbersInRange = 0

while noNneedExit:
    enteredNumber = int(input("Enter number: "))
    if enteredNumber == P or enteredNumber == H:
        noNneedExit = False
    if enteredNumber < P:
        sumEnteredIfLessP += enteredNumber
    if enteredNumber > H:
        productOgNumMoreH = productOgNumMoreH * enteredNumber
    for i in range(P, H):
        countNumbersInRange = countNumbersInRange + 1

print("Sum of numbers less than P = ",sumEnteredIfLessP)
print("Product of numbers more than H = ",productOgNumMoreH)
print("Number of numbers in range of values from P to H is ",countNumbersInRange)