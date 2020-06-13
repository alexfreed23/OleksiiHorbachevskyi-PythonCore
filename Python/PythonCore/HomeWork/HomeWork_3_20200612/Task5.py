#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:31:27 2020

@author: oleksiy

without checking if user enter letters

"""

money = int(input("Enter value of UAN to exchange:"))

if money % 200 == 0:
    print("To exchange ", money, " needed ", money // 200, " banknote(s) of 200 UAH")
elif money % 200 != 0 and money % 100 == 0:
    print("To exchange ", money, " needed ", money // 200, "banknote(s) of 200 UAH \
and ", (money % 200) // 100, " 100 UAH banknote(s)")
elif money % 200 != 0 and money % 100 != 0 and money % 10 == 0:
    print("To exchange ", money, " needed ", money // 200, "banknote(s) of 200 UAH  \
and ", (money % 200) // 100, " 100 UAH banknote(s) and ", ((money % 200) % 100) // 10, "banknote(s) of 10 UAN")
elif money % 200 != 0 and money % 100 != 0 and money % 10 != 0:
    print("To exchange ", money, " needed \n", money // 200, "banknote(s) of 200 UAH and \n", (money % 200) // 100, "banknote(s) of 100 UAH and \n", ((money % 200) % 100) // 10, "banknote(s) of 10 UAN and \n", ((money % 200) % 100) % 10, "banknote(s) of 1 UAH")
