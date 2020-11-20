# -*- coding: utf-8 -*-
"""
@author: Harold
"""


import scrapy
from bs4 import BeautifulSoup
import re

class ActuSpider(scrapy.Spider):
    name = 'Actu'
    
    
    def __init__(self):  
        self.num = 0
        self.urls = [
            'http://actucameroun.com',
        ]
    
        self.scrapper_urls = []


    def start_requests(self):
        while len(self.urls) != 0:
            for url in self.urls:
                yield scrapy.Request(url=url, callback=self.crawl_all_links_of_web_site)     
        

    def crawl_specifique_web_site_links(self, response):
        self.num = self.num+1
        page = response.css('title::text').get()
        filename = f'Actu-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
        
        
    def crawl_all_links_of_web_site(self, response):
        self.num = self.num+1
        body = response.body
        url = response.url
        page = response.css('title::text').get()
        filename = f'Actu-{page}.html'
        with open(filename, 'wb') as f:
            f.write(body)
        self.log(f'Saved file {filename}')
        self.scrapper_urls.append(url)
        soup = BeautifulSoup(body, features="lxml")
        for link in soup.find_all('a'):
            link = link.get('href')
            if  link not in self.scrapper_urls:
                protocole_test = re.match('http[s]?', link)
                if protocole_test:
                    self.urls.append(link)
                else:
                    self.urls.append(url.strip('/') + link)
        self.urls.remove(url)