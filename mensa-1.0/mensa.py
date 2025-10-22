
#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from datetime import date

# URL der Mensa
url = "https://www.mensaplan.de/potsdam/mensa-griebnitzsee/index.html"

# Webseite abrufen
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Heutiges Datum als Textformat wie auf der Seite
heute = date.today().strftime("%d.%m.%Y")

# Tabelle mit Speiseplan finden
tabelle = soup.find("table", class_="aw-weekly-menu")


today_cells = tabelle.find_all("td",class_="today")
print(today_cells[1].text)
print(today_cells[2].text)
print(today_cells[5].text)
print(today_cells[6].text)

