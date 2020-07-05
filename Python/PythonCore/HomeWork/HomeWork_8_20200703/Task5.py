#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 11:30:28 2020

@author: oleksiy
"""


def is_year_leap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(is_year_leap(int(input("Enter year to check if it is leap: "))))