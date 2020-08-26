# -*- coding: utf-8 -*-
import scrapy
from datetime import date

class HiltimesSpider(scrapy.Spider):
    name = 'hilltimes_crawl'
    start_urls = ['https://www.hilltimes.com/news']

    def parse(self, response):
        quotes = response.xpath('//*[@class="htitle4"]')
        
        for quote in quotes:
            yield {
                  'title': quote.xpath('.//a/text()').get(),
                  'date': str(date.today()),
                  'source':'Hilltimes',                  
                  'link': response.urljoin(quote.xpath('.//a/@href').get()),
            }
