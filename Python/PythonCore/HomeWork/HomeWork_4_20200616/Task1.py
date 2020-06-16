#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:42:45 2020

@author: oleksiy
"""

import random

secretNumber = random.randint(0, 100)
tryNumber = 1
while tryNumber <=10:
    userNumber = int(input("Enter your number: "))
    if userNumber < secretNumber:
        print("Your number is less than SECRET NUMBER")
    elif userNumber > secretNumber:
        print("Your number is more than SECRET NUMBER")
    else:
        print("Absolutely RIGHT!!!")
        break
    tryNumber +=1 
print("Secret number is: ", secretNumber)
