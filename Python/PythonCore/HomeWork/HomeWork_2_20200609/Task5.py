#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:28:21 2020

@author: oleksiy
"""
import math

katet_1 = input("Enter first right triangle's side:\n")
katet_2 = input("Enter second right triangle's side:\n")

print("Hypotenuse of your triangle is: ", math.sqrt((int(katet_1)**2)+(int(katet_2)**2)))