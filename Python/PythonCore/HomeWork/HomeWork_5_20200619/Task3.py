#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 01:28:52 2020

@author: oleksiy
"""

enteredValue = input("Enter value: ")
myList = list(enteredValue)
newNumber = ""
product = 1
product2 = 1

for element in myList:
    product = product * int(element)
print("Product of digits of entered value:", product)

i = 0
count = len(myList) - 1 

while count >= 0:
    newNumber = newNumber + myList[count]
    product2 = product2 * int(myList[count])
    print("i: ", i,"count: ",count,"newNumber: ",newNumber, "product2: ",product2)
    i = i + 1
    count = count - 1
    
print("Revers of entered value is ",newNumber, " Product of digits reversed value is ", product2)