#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:55:26 2020

@author: oleksiy

To determine whether a year is a leap year, follow these steps:

1) If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
2) If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
3) If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
4) The year is a leap year (it has 366 days).
5) The year is not a leap year (it has 365 days).


"""

year = int(input("Enter year: "))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("The year is a leap year (it has 366 days)")
        else:
            print("The year is not a leap year (it has 365 days).")
    else:
        print("The year is a leap year (it has 366 days)")
else:
    print("The year is not a leap year (it has 365 days)")