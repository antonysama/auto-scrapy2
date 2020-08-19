# -*- coding: utf-8 -*-
import scrapy
from datetime import date

class CbocSpider(scrapy.Spider):
    name = 'cboc_crawl'
    start_urls = ['https://www.conferenceboard.ca/press/default.aspx']

    def parse(self, response):
        quotes = response.xpath('//*[@data-sf-field="Title"]')
        
        for quote in quotes:
            yield {
                  'title': quote.xpath('.//text()').get(),
                  'date': str(date.today()),
                  'source':'CboC',                  
                  'link': response.urljoin(quote.xpath('.//@href').get()),
            }
