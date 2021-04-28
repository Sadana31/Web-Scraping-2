from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

# getting data and finding table
page = requests.get(url)
soup = bs(page.text,'html.parser')
star_table = soup.find_all('table')

# getting data from table <td> and <tr> tag
temp_array= []
table_rows = star_table[4].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_array.append(row)

# creating arrays for storing respective data
star_names = []
distance =[]
mass = []
Radius =[]


# adding values to lists
for i in range(1,len(temp_array)):
    star_names.append(temp_array[i][0])
    distance.append(temp_array[i][5])
    mass.append(temp_array[i][7])
    Radius.append(temp_array[i][8])

# creating the csv file
df2 = pd.DataFrame(list(zip(star_names,distance,mass,Radius,)),
columns=['Star_name','distance_from_earth','star_mass','star_radius'])
df2.to_csv('dwarf_stars.csv')