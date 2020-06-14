#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 20:47:17 2020

@author: oleksiy
"""
import math

figure = input("Please select figure and enter respective number:\n 1 - rectangle\n 2 - triangle\n 3 - circle\n")

if int(figure) == 1:
    width = float(input("Enter width:\n"))
    hight = float(input("Enter hight:\n"))
    print("The square of rectangle is: ", width*hight)
elif int(figure) == 2:
    side1 = float(input("Enter side 1:\n"))
    side2 = float(input("Enter side 2:\n"))
    side3 = float(input("Enter side 3:\n"))
    p = (side1 + side2 + side3)/2
    print("The square of triangle is: ",math.sqrt(p*(p - side1)*(p - side2)*(p - side3)))
elif int(figure) == 3:
    radius = float(input("Enter radius:\n"))
    print("The square of circle is: ", math.pi * radius**2)
else:
    print("Entered value is not correct")