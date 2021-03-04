# -*- coding: utf-8 -*-
"""
@author: Harold
"""


import scrapy
from bs4 import BeautifulSoup
import re
from googleapi import google

links = []
num_page = 10
search_results = google.search("cameroun", num_page)
for result in search_results :
    links.append(result.link)

class ActuSpider(scrapy.Spider):
    name = 'CMR'

    def __init__(self):
        self.num = 0
        self.urls = links
        self.scrapper_urls = []


    def start_requests(self):
        while len(self.urls) != 0:
            for url in self.urls:
                yield scrapy.Request(url=url, callback=self.crawl_all_links_of_web_site)     
    
    # Pour enregistrer juste la page du site actuel, decommenter les lignes suivantes
    	#et remplacer "crawl_all_links_of_web_site" de la ligne superieure par "crawl_specifique_web_site_links"

    # def crawl_specifique_web_site_links(self, response):
    #     self.num = self.num+1
    #     page = response.css('title::text').get()
    #     filename = f'CMR-{page}.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log(f'Saved file {filename}')
        
    #Pour parourir les sites internes aux sites specifies

    def crawl_all_links_of_web_site(self, response):
        self.num = self.num+1
        body = response.body
        url = response.url
        page = response.css('title::text').get()
        filename = f"CMR-{page}.html"
        with open(filename, 'wb') as f:
            f.write(body)
        self.log(f"Saved file {filename}")
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