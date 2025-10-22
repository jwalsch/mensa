#!/usr/bin/env python3
import argparse
from bs4 import BeautifulSoup
import requests
from datetime import date

parser = argparse.ArgumentParser(description="parser")
parser.add_argument("--today", action="store_true", help="Speiseplan heute")
parser.add_argument("--week", action="store_true", help="Speiseplan woche")
args = parser.parse_args()
# URL der Mensa
url = "https://www.mensaplan.de/potsdam/mensa-griebnitzsee/index.html"

# Webseite abrufen
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Heutiges Datum als Textformat wie auf der Seite
heute = date.today().strftime("%d.%m.%Y")

# Tabelle mit Speiseplan finden
tabelle = soup.find("table", class_="aw-weekly-menu")

if args.today:
    today_cells = tabelle.find_all("td",class_="today")
    print(today_cells[6].text)
    print(today_cells[8].text)
    print(today_cells[12].text)
    print(today_cells[13].text)
elif args.week:
    for td in tabelle.find_all("td"):
        print(td.text)

