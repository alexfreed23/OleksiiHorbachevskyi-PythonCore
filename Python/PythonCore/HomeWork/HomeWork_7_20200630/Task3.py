#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 23:26:48 2020

@author: oleksiy
"""

dictionaryOfCountreisCities = {"Ukraine" : ["Kyiv", "Kharkiv", "Odesa", \
    "Dnipro", "Donetsk", "Zaporizhia", "Lviv"],"France" : ["Paris", \
    "Marseille", "Lyon", "Toulouse", "Nice", "Nantes"], "Italy" : ["Rome", \
    "Milan", "Naples", "Turin", "Palermo", "Genoa"], "Germany" : ["Berlin", \
    "Hamburg", "Munich", "Cologne", "Frankfurt am Main", "Stuttgart"], \
    "Portugal" : ["Abrantes", "Albufeira", "Alfena", "Almada", ], \
    "United Kingdom" : ["London", "Bradford", "Cambridge", "Chester", \
    "Derby", "Liverpool", "Manchester"] }

print("You can choose city from this list: \nKyiv, Kharkiv, Odesa, Dnipro, \
Donetsk, Zaporizhia, \nLviv,Paris, Marseille, Lyon, Toulouse, Nice, \
Nantes,Rome, Milan, \nNaples, Turin, Palermo, Genoa,Berlin, Hamburg, \
Munich, Cologne, Frankfurt am Main, \nStuttgart,Abrantes, Albufeira, \
Alfena, Almada,London, Bradford, \nCambridge, Chester, Derby, Liverpool, \
Manchester")
eneterCity = input("Enter city to identify Country: ")

for element in dictionaryOfCountreisCities.keys():
    if eneterCity in dictionaryOfCountreisCities[element]:
        print(eneterCity, "belongs to ", element)
        break