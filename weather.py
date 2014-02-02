#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# Prints the following basic weather data:
# - City name
# - Weather conditions (e.g. rain, cloudy, etc.)
# - Temperature (current, hi, lo)
#
# Weather data source: OpenWeatherMap http://openweathermap.org (API v2.5)
#
# Copyright 2013 Dennis Ideler <ideler.dennis@gmail.com>

from colorama import init, Fore, Back, Style
import requests
import sys

# Set up parameters and download data.
CITY_ID = 6155721 # St. Catharines, Ontario, Canada.
UNITS = 'metric' # Celsius (use 'imperial' for Fahrenheit).
QUERY = '?id={}&units={}'.format(CITY_ID, UNITS)
URL = 'http://api.openweathermap.org/data/2.5/weather{}'.format(QUERY)

try:
    json = requests.get(URL).json()
except:
    print("Oh no, the request failed. Possible causes:\n"
          "- Disconnected from the internet\n"
          "- URL is invalid\n"
          "- Website is down or doesn't exist")
    sys.exit(1)

# Extract relevant data from the JSON.
city_name = json['name']

descriptions = []
for weather in json['weather']:
    descriptions.append(weather['description'])
weather_conditions = ', '.join(descriptions).capitalize()

temp = round(json['main']['temp'])
temp_min = round(json['main']['temp_min'])
temp_max = round(json['main']['temp_max'])

# Print weather data using colorama.
init(strip=not sys.stdout.isatty()) # Strip colors if stdout is redirected.

line1 = '{}{}{}\n'.format(Style.BRIGHT, city_name, Style.RESET_ALL)
line2 = '{}{}°{} {}{}°{} {}{}°{}\n'.format(Fore.GREEN, temp, Fore.RESET,
                                           Fore.RED, temp_max, Fore.RESET,
                                           Fore.BLUE, temp_min, Fore.RESET)
line3 = '{}{}{}'.format(Style.DIM, weather_conditions, Style.RESET_ALL)
print(line1 + line2 + line3)
