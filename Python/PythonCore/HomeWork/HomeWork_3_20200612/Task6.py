#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 23:07:09 2020

@author: oleksiy

Scheme of places taken from this article
https://touristam.com/mesta-v-vagone-platskart-raspolozhenie.html

Image1: https://touristam.com/wp-content/uploads/2018/12/mesta-v-vagone-platskart-raspolozhenie-5.jpg
Image2: https://touristam.com/wp-content/uploads/2018/12/mesta-v-vagone-platskart-raspolozhenie-1.jpg

"""

try:
    placeNumber = int(input("Enter place number:"))
    if placeNumber < 37 and placeNumber > 0:
        coupeOrSide = "comparment place"
    elif placeNumber > 36 and placeNumber <= 54:
        coupeOrSide = "side place"
    elif placeNumber > 54 or placeNumber <=0:
        coupeOrSide = "No such place"
    
    if placeNumber % 2 == 0 and placeNumber <= 54 and placeNumber > 0:
        placeUpDown = "place is UP"
    elif placeNumber % 2 != 0 and placeNumber <= 54 and placeNumber > 0:
        placeUpDown = "place is DOWN"
    else:
        placeUpDown = "we cannot idetify Up or Down it is"

    print(coupeOrSide," and ", placeUpDown)

except ValueError:
    print("That's not a number")