#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 01:44:18 2020

@author: oleksiy
"""

def is_prime(number):
    isPrime = False
    for num in range(1, number+1):
        if num != 1 and num != number:
            if number % num == 0:
                print("Is NOT PRIME",number,num, number % num )
                isPrime = False
                return isPrime
            else:
                print("Is PRIME", number,num, number % num )
                isPrime = True
    return isPrime

print(is_prime(182))