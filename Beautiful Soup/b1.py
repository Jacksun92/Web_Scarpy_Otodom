import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

mazowieckie_for_sale = []

for x in range(1, 3):
    url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/mazowieckie?page='
    r = requests.get(url+str(x))

    soup = BeautifulSoup(r.content, 'html.parser')
    content = soup.find_all('li', class_='css-p74l73 es62z2j17')

    for property in content:
        name = property.find('h3').text
        location = property.find('span', class_='css-17o293g es62z2j9').text
        price = property.find('span', class_='css-rmqm02 eclomwz0').text

        property_specs = {
            'name': name,
            'location': location,
            'price': price
        }
        mazowieckie_for_sale.append(property_specs)
    time.sleep(2)
df = pd.DataFrame(mazowieckie_for_sale)
print(df.head())

df.to_excel('mazowieckie_for_sale1.xlsx')
