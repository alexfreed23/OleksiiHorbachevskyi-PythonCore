#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 18:48:40 2020

@author: oleksii
"""

from pyowm.owm import OWM

city = input("Please enter city: \n")
owm = OWM('558389224c7b46b0434be8ef3129403b')
try:
    mgr = owm.weather_manager()
    weather = mgr.weather_at_place(city).weather  # get the weather at London,GB now
    dump_dict = weather.to_dict()
    humidityInCiyty = str(dump_dict['humidity'])
    windSpeed = str(dump_dict['wind']['speed'])
    temperature = str(int(dump_dict['temperature']['temp']) - 273.15) 
    print("Weather in", city, "is: \n ----------------- \n temperature", round(float(temperature), 0), "C \n humidity is", humidityInCiyty, "% \n Wind speed is", windSpeed, "meters per second \n -----------------")
except Exception:
    print("City not found!")
