import datetime

from bs4 import BeautifulSoup

from database.DB_util import MongoDB
from scripts.scraper import simple_get

# This script will scrape the current situation in Canada
now = datetime.datetime.now()
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
                             , "probable": row.select('td')[2].text, "day": now.day, "month": now.month, "year": now.year})
    else:
        provinces.append({"province": row.select('td')[0].text, "confirmed": row.select('td')[1].text
                         , "probable": row.select('td')[2].text, "day": now.day, "month": now.month, "year": now.year})


total_tests_table = current_situation_div.select('table')[1]
tests_tbody = total_tests_table.select('tbody')[0]
for row in tests_tbody.select('tr'):
    provinces.append({"total_patients_tested": int((row.select('td')[0].text).replace(',', ""))
                         , "total_positives": int((row.select('td')[1].text).replace(',', ""))
                         , "total_negative": int((row.select('td')[2].text).replace(',', ""))
                         , "day": now.day, "month": now.month, "year": now.year})


instance = MongoDB.getInstance()
instance.create_docs(provinces, "current_situation")
print(">>>>     Current Situation Scraping Done !!!    >>>>>")



