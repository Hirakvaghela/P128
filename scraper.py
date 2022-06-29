from bs4 import BeautifulSoup 
import requests 
import pandas as pd

brown_dwarf_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(brown_dwarf_url)
print(page)

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all('table')
print(len(table))

temporary_list = []

table_rows = table[4].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temporary_list.append(row)
print(temporary_list)

Star_name = []
Dwarf = []
Constellation = []
Distance = []
Radius = []

for i in range(1, len(temporary_list)):
    Star_name.append(temporary_list[i][0])
    Dwarf.append(temporary_list[i][7])
    Constellation.append(temporary_list[i][1])
    Distance.append(temporary_list[i][5])
    Radius.append(temporary_list[i][8])

df2 = pd.DataFrame(list(zip(Star_name, Dwarf, Constellation, Distance, Radius)), columns=['Star_name', 'Dwarf_name', 'Constellation', 'Distance', 'Radius'])
print(df2)

df2.to_csv('brown_dwarfs.csv') 