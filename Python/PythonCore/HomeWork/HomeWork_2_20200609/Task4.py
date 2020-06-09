#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:20:29 2020

@author: oleksiy
"""
import math

radius = input("Enter radius of circle:\n")

print("Perimetr of circle is: ", 2*math.pi*int(radius))
print("Area of circle is: ", math.pi*(int(radius)**2))
