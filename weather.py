#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# Prints the following basic weather data:
# - Weather conditions (e.g. rain, cloudy, etc.)
# - Temperature (current, hi, lo)
#
# Weather data source: OpenWeatherMap http://openweathermap.org (API v2.5)
#
# Copyright 2017 by David Laubenstein 

from colorama import init, Fore, Back, Style
import requests
import sys

# Set up parameters and download data.
CITY_ID = str('2892794') # St. Catharines, Ontario, Canada.
UNITS = 'metric' # Celsius (use 'imperial' for Fahrenheit).
APP_ID = str('7aa91ff4cf71825f909554def466be78')
#handle arguments. and set parameter COUND and COUNT_Info
if (len(sys.argv) == 2):  
    COUNT = str(int(sys.argv[1]) + 1)

    try: 
        if (int(sys.argv[1]) <= 16):
            if(int(sys.argv[1] != 0)):
                COUNT_INFO = int(sys.argv[1])
            else:
                COUNT_INFO = 0
        else:
            sys.exit(1)

    except:
        print("The argument you entered is not valid! \n"
	      "You have to enter an Integer between 0 and 16, which is the \n"
	      "days after today... ")
        sys.exit(1)

elif (len(sys.argv) == 1):
    COUNT = "0";
    COUNT_INFO = 0;
else:
    sys.exit(1)

QUERY = '?id={}&units={}'.format(CITY_ID, UNITS)
URL = 'http://api.openweathermap.org/data/2.5/forecast/daily?id='+CITY_ID+'&APPID='+APP_ID+'&cnt='+COUNT+''.format(QUERY)
try:
    json = requests.get(URL).json()
except:
    print("Oh no, the request failed. Possible causes:\n"
          "- Disconnected from the internet\n"
          "- URL is invalid\n"
          "- Website is down or doesn't exist")
    sys.exit(1)

# Extract relevant data from the JSON.
city_name = json['city']['name']
descriptions = []
for weather in json['list'][COUNT_INFO]['weather']:
    descriptions.append(weather['description'])
weather_conditions = ', '.join(descriptions).capitalize()
temp = json['list'][COUNT_INFO]['temp']['day'] - 273
temp_int = str(int(temp))
current = '{}°, {}'.format(temp_int, weather_conditions,)
#print(temp_int + '°')
print(current)
