import requests
import scrapy
from bs4 import BeautifulSoup


# 'scrapy crawl allhomes'
# to run, write in terminal -> scrapy crawl allhomes -o output.xlsx

class AllhomesSpider(scrapy.Spider):
    name = 'allhomes'
    allowed_domains = ['otodom.pl']
    start_urls = ['https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/mazowieckie?page=1']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        content = soup.find_all('li', {'class': 'css-p74l73 es62z2j17'})

        for property in content:
            yield {
                'name': property.find('h3').text,
                'location': property.find('span', {'class': 'css-17o293g es62z2j9'}).text,
                'price': property.find('span', {'class': 'css-rmqm02 eclomwz0'}).text
            }

        for x in range(2, 101):
            next_page = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/mazowieckie?page=' + str(x)
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
