#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:28:04 2020

@author: oleksiy
"""
def checkDate(day, month, year):
    dayInMonth = [31,28,31,30,31,30,30,31,31,30,31,30,31]
    if month < 1 or month > 12: return False
    elif day < 1 or day > 31: return False
    elif month > dayInMonth[month]: 
        print(month, dayInMonth[month-1])
        return False
    elif len(year) > 4 or len(year) < 4: return False
    else:
        print(month, dayInMonth[month-1])
        return True

print(checkDate(int(input("Enter day: ")),int(input("Enter month: ")), input("Enter year: ")))