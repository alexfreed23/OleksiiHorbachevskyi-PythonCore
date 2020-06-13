#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 18:45:29 2020

@author: oleksiy
"""
import math

R = float(input("Enter radius of circle: \n"))
S = float(input("Enter square of square rectangle: \n"))
K = float(input("Enter minnimum passade: \n"))

if (math.sqrt(S) - 2*R) >= K*2:
    print("Round stage CAN be placed in square hall!")
else:
    print("Round stage CANNOT be placed in square hall!")