# -*- coding: utf-8 -*-
import scrapy
from datetime import date

class DeloitteSpider(scrapy.Spider):
    name = 'deloitte_crawl'
    start_urls = ['https://www2.deloitte.com/ca/en/pages/press-releases/topics/newsroom.html?icid=bottom_newsroom']

    def parse(self, response):
        quotes = response.xpath('//*[@class="article-text"]')
        
        for quote in quotes:
            yield {
                  'title': quote.xpath('.//h2/text()').get(),
                  'date': str(date.today()),
                  'source':'Deloitte',
                  'link': response.urljoin(quote.xpath('.//parent::div/parent::a/@href').get(),
            }
