
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

from scripts.scraper import simple_get

raw_html = simple_get('https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection.html')
html = BeautifulSoup(raw_html, 'html.parser')
body = html.select('body')[0]
main = body.select('main')[0]
current_situation_div = main.select('div')[4]
table = current_situation_div.select('table')[0]
tbody = table.select('tbody')[0]
provinces = []
for row in tbody.select('tr'):
    if row.select('td')[0].text == 'Total cases':
        provinces.append({"total_cases": row.select('td')[0].text, "confirmed": row.select('td')[1].text
                             , "probable": row.select('td')[2].text})
    else:
        provinces.append({"province": row.select('td')[0].text, "confirmed": row.select('td')[1].text
                         , "probable": row.select('td')[2].text})

print(provinces)


