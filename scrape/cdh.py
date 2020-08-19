# -*- coding: utf-8 -*-
import scrapy
from datetime import date

class CdhoweSpider(scrapy.Spider):
    name = 'cdhowe_crawl'
    start_urls = ['https://www.cdhowe.org/research-insights']

    def parse(self, response):
        quotes = response.xpath('//*[@class="imagebox__title"]')
        
        for quote in quotes:
            yield {
                  'title': quote.xpath('.//a/text()').get(),
                  'date': str(date.today()),
                  'source':'CD_Howe',
                  'link': response.urljoin(quote.xpath('.//a/@href').get()),
            }