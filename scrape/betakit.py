# -*- coding: utf-8 -*-
import scrapy
from datetime import date

class BetakitSpider(scrapy.Spider):
    name = 'betakit_crawl'
    start_urls = ['https://betakit.com']

    def parse(self, response):
        quotes = response.xpath('//*[@class="entry-title"]')
        
        for quote in quotes:
            yield {
                  'title': quote.xpath('.//a/text()').get(),
                  'date': str(date.today()),
                  'source':'Betakit',                  
                  'link': response.urljoin(quote.xpath('.//a/@href').get()),
            }
