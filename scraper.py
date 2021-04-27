# importing necessary modules
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv
import numpy as np

# getting data from url
page = requests.get("https://en.wikipedia.org/wiki/Dwarf_planet")

# accessing the table data
soup = bs(page.text,'html.parser')
table_data = soup.find('table',{"style":"width: 100%; margin: 0;"})


# getting data from rows
planet_data = table_data.find_all('tr')
# empty array for adding data temporarily
temp_array = []

# initializing different arrays
names = []
region = []
orb_rad = []
orb_period = []
orb_speed = []
inclination = []
eccentricity = []

# getting data and adding to temp_array
for tr in planet_data:
    data = tr.find_all("td")
    data = [i.text.rstrip() for i in data]
    temp_array.append(data)
    # finding the name from <a> tag
    name = tr.find_all("a",href=True)[0]["title"]
    names.append(name)

# headers name
headers=["dwarf_planet_name","orb_rad","orb_period","orb_speed","inclination","eccentricity"]

# adding values to respected list
for i in range(1,len(temp_array)):
    region.append(temp_array[i][0])
    orb_rad.append(temp_array[i][1])
    orb_period.append(temp_array[i][2])
    orb_speed.append(temp_array[i][3])
    inclination.append(temp_array[i][4])
    eccentricity.append(temp_array[i][5])

# writing csv file
planet_info = pd.DataFrame(list(zip(names,orb_rad,orb_period,orb_speed,inclination,eccentricity)),
columns=["dwarf_planet_name","orb_rad","orb_period","orb_speed","inclination","eccentricity"])

planet_info.to_csv("dwarf_planets_data.csv")

