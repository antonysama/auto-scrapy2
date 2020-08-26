# -*- coding: utf-8 -*-
import scrapy
from datetime import date

class GlobeSpider(scrapy.Spider):
    name = 'globe_crawl'
    start_urls = ['https://www.theglobeandmail.com/business']

    def parse(self, response):
        quotes = response.xpath('//*[@class="c-card"]')
        
        for quote in quotes:
            yield {
                  'title': quote.xpath('.//a/div/div/div/text()').get(),
                  'date': str(date.today()),
                  'source':'Globe', 
                  'link': response.urljoin(quote.xpath('.//a/@href').get()),
            }
