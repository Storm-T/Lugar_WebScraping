import scrapy
import logging


class LugarsarlSpider(scrapy.Spider):
    name = 'lugarsarl'
    allowed_domains = ['lugarsarl.com']
    start_urls = ['http://lugarsarl.com/']

    def parse(self, response):
        page = response.css('title::text').getall()
        print(page)
        logging.info(page)
        # filename = f'lugar-{page}.html'
        filename = f'lugarsarl.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'saved file {filename}')

    def start_requests(self):
        urls = [
            'http://www.lugarsarl.com' 
        ]

        for url in urls: 
            yield scrapy.Request(url=url, callback=self.parse)

