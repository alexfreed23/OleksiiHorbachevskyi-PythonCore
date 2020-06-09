#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:37:53 2020

@author: oleksiy
"""
# Task6.1
catsCollection = ["cat1", "cat2", "cat3", "cat3"]
carsCollection = ["car1", "car2", "car3"]
elephantsCollection = ["elephant1", "elephant2", "elephant3"]


collections = dict((("cats", catsCollection), ("cars", carsCollection), ("elephants", elephantsCollection)))

# "I think the best way saving such type of information in ditcionary"
print(type(collections))
print(collections["cats"])
print(collections["cars"])
print(collections["elephants"])


# Task6.2 - to save uniq elements of collection
uniqCatsCollection = set(collections["cats"])

print(uniqCatsCollection)