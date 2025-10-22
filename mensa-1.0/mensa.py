#!/usr/bin/env python3
import argparse
from bs4 import BeautifulSoup
import requests
from datetime import date

parser = argparse.ArgumentParser(description="parser")
parser.add_argument("--today_gr", action="store_true", help="Speiseplan heute griebnitzsee")
parser.add_argument("--today_go", action="store_true", help="Speiseplan heute golm")
parser.add_argument("--today_np", action="store_true", help="Speiseplan heute neues palais")
parser.add_argument("--week", action="store_true", help="Speiseplan woche")
args = parser.parse_args()
# URL der Mensa
if args.today_gr:
    uni = "griebnitzsee"
elif args.today_go:
    uni = "golm"
elif args.today_np:
    uni = "am-neuen-palais"
else:
    raise SystemExit("bitte --today-gr oder today-go eingeben")
url = f"https://www.mensaplan.de/potsdam/mensa-{uni}/index.html"

# Webseite abrufen
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Heutiges Datum als Textformat wie auf der Seite
heute = date.today().strftime("%d.%m.%Y")

# Tabelle mit Speiseplan finden
tabelle = soup.find("table", class_="aw-weekly-menu")

if args.today_gr:
    today_cells = tabelle.find_all("td",class_="today")
    print(today_cells[6].text)
    print(today_cells[8].text)
    print(today_cells[12].text)
    print(today_cells[13].text)
elif args.today_go:
    today_cells = tabelle.find_all("td",class_="today")
    print(today_cells[1].text)
    print(today_cells[2].text)
    print(today_cells[3].text)
    print(today_cells[4].text)
elif args.today_np:
    today_cells = tabelle.find_all("td",class_="today")
    print(today_cells[1].text)
    print(today_cells[2].text)
    print(today_cells[3].text)
    print(today_cells[4].text)
elif args.week:
    for td in tabelle.find_all("td"):
        print(td.text)

