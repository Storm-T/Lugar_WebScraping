# spider pour récuperer toutes les pages du site de Lugar
# et les stocker

import scrapy


class LugarSpider(scrapy.spiders):
    name = "lugar"

    def start_requests(self):
        url = 'http://www.lugarsalr.com'

        for url in url:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.css('title::text').getall()
        filename = f'lugar-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.all)
        self.log(f'saved file {filename}')
