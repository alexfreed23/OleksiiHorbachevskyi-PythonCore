#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:18:39 2020

@author: oleksiy
"""

def countValueOnDeposit(n, years):
    depositValue = n
    for year in range(years):
        depositValue = depositValue + (depositValue * 0.1)
    return depositValue

print(countValueOnDeposit(float(input("Enter how many money do \
you want to put on deposit: ")), \
                          int(input("Enter years for deposit: "))))
