import requests, re, sys
from bs4 import BeautifulSoup

html = requests.get('https://leagueoflegends.fandom.com/wiki/List_of_champions/Base_statistics')
soup = BeautifulSoup(html.content,'html.parser')

table = soup.table.find_all('tr')
header = table[0]
body = table[1:]

fieldnames = [h.get_text().strip() for h in header.find_all('th')]

import csv

with open(sys.argv[1],'w') as csv_file:
    writer = csv.DictWriter(csv_file,delimiter=',',fieldnames=fieldnames)
    writer.writeheader()
    for tr in body:
        tds = tr.find_all('td')
        champ_name = tds[0].get_text().strip().split()[0]
        stats = tds[1:]
        line = [champ_name]+[re.sub(r'[+%]',r'',stat.get_text().strip()) for stat in stats]
        writer.writerow(dict(zip(fieldnames,line)))
