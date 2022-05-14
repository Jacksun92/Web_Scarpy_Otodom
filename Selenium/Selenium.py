# -*- coding: utf-8 -*-
from urllib import response
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
from bs4 import BeautifulSoup

name = 'dom'  # if you use base of spider but want to scrape other page, you need to updatenem of the spider
allowed_domains = ['otodom.pl']
start_urls = ['http://otodom.pl/']

driver = webdriver.Chrome()
driver.get('https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/mazowieckie?page=1')
sleep(3)

Button = driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
Button.click()


def parse(self, response):
    soup = BeautifulSoup(response.text, 'lxml')
    contents = soup.find_all('li', {'class': 'css-p74l73 es62z2j17'})

    for content in contents:
        title = content.find_element(By.XPATH,
                                     '//*[@id="__next"]/div[2]/main/div[1]/div[3]/div[1]/div[2]/div[2]/ul/li[1]/a/article/div[1]/h3').text
        price = content.find_element(By.XPATH,
                                     './/*[@id="__next"]/div[2]/main/div[1]/div[3]/div[1]/div[2]/div[2]/ul/li[1]/a/article/div[2]/span[1]').text
        location = content.find_element(By.XPATH,
                                        './/*[@id="__next"]/div[2]/main/div[1]/div[3]/div[1]/div[2]/div[2]/ul/li[1]/a/article/p/span').text
        print(title, price, location)

    for url in range(2, 3):
        next_page = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/mazowieckie?page=' + str(url)
        next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse)
