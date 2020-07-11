#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 19:47:41 2020

@author: oleksiy
"""

# Fishing


class Pond():
    capacity = []
    state = 'poor'                               # poor, normal, rish

    def obtainFish(self, fish):
        return self.capacity.append(fish)
    
    def lostFish(self, fish):
        return self.capacity.remove(fish)
    
    def showCapacity(self):
        return len(self.capacity)
    
    def showState(self):
        return self.state
    
class Fish():
    weight = 0

class SheatFish(Fish):
    whiskerLength=10
        
    
class Carp(Fish):
    color='white'
    
    

menu = '0'

myPond = Pond()

print("1. View capacity;\n" +
      "2. View state of Pond;\n" +
      "3. Add fish( Carp or SheatFish);\n" +
      "4. Catch fish (concrete instance);\n" +
      "5. Create new fish (fill himself the creator)))\n" +
      "6. Finish the game.\n\n")

while menu != '6':
    menu = input("Enter number of menu: ".upper())
    
    if menu == '1':
        print(myPond.showCapacity())
    elif menu == '2':
        print(myPond.showState())
    elif menu == '3':
        newFish = input("Enter whish fish to add [Carp] or [SheatFish]: ")
        if newFish == 'Carp':
            myPond.obtainFish(Carp())
        elif newFish == 'SheatFish':
            myPond.obtainFish(SheatFish())
        else:
            print("Unable to add sach fish to the Pond...")
        if myPond.showCapacity() <= 5 and myPond.showCapacity() > 0: myPond.state = 'poor'
        if myPond.showCapacity() > 5 and myPond.showCapacity() < 10: myPond.state = 'normal'
        if myPond.showCapacity() >= 10: myPond.state = 'rich'
    elif menu == '4':
        cutchFish = input("Enter whish fish to cutch [Carp] or [SheatFish]: ")
        if cutchFish == 'Carp':
            for fishInList in myPond.capacity:
                if isinstance(fishInList, Carp): 
                    myPond.lostFish(fishInList)
                    break
            #myPond.lostFish(Carp())
        elif cutchFish == 'SheatFish':
            for fishInList in myPond.capacity:
                if isinstance(fishInList, SheatFish):
                    myPond.lostFish(fishInList)
                    break
        else:
            print("Unable to cutch sach fish to the Pond...")
        if myPond.showCapacity() <= 5 and myPond.showCapacity() > 0: myPond.state = 'poor'
        if myPond.showCapacity() > 5 and myPond.showCapacity() < 10: myPond.state = 'normal'
        if myPond.showCapacity() >= 10: myPond.state = 'rich'
    elif menu == '5':
        fishName = input("Enter name your fish: ")
        
        class newFish(Fish):
            myNewFishName = fishName
            
        print("You created new fish: ", newFish.myNewFishName)
    else:
        menu = '6'
        print("Exit..")
    