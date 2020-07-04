#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:05:23 2020

@author: oleksiy
"""

def makeOperationsWithNumbers(number_1, number_2, operation):
    if operation == "+": return number_1 + number_2
    elif operation == "-": return number_1 - number_2
    elif operation == "*": return number_1 * number_2
    elif operation == "/": 
        if number_2 != 0:
            return number_1 / number_2
        else:
            print("Unable divide by zero")
            return 0
    else:
        print("Unknown operation")
        return 0

print(makeOperationsWithNumbers(float(input("enter number 1: ")), \
                                float(input("enter number 2: ")), \
                                    input("Enter opetarion:")))