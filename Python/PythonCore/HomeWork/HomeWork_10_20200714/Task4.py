#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 20:57:35 2020

@author: oleksii
"""

import random

elementsCount = random.randint(3,10)
print("Genertated list which consist of",elementsCount, "elements")
firstList = []
for i in range(elementsCount):
    addElement = random.randint(0,10)
    firstList.append(addElement)


usersList = list(input("Please enter your list splitted by comma with " +
            str(len(firstList)) + " elements: ").replace(',', '').replace(' ', ''))
usersListInt = []
for element in usersList:
    try:
        usersListInt.append(int(element))
    except ValueError:
        print("list should contains only numbers")


newListWithSums = []
for num in range(0,len(firstList)):
    newListWithSums.append(firstList[num] + usersListInt[num])
    num += 1


print("Random list: \n", firstList)
print("Entered list by user: \n",usersListInt)
print("List of sums related elements of lists: \n", newListWithSums)
