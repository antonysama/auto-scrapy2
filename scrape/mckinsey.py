# -*- coding: utf-8 -*-
import scrapy
from datetime import date

class MckinseySpider(scrapy.Spider):
    name = 'mckinsey_crawl'
    start_urls = ['https://www.mckinsey.com/featured-insights']

    def parse(self, response):
        quotes = response.xpath('//*[@class="text-wrapper"]')
        
        for quote in quotes:
            yield {
                  'title': quote.xpath('.//div/text()').get(),
                  'date': str(date.today()),
                  'source':'Mckinsey',                  
                  'link': response.urljoin(quote.xpath('.//@href').get()),
            }
