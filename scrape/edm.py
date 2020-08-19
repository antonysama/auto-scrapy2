# -*- coding: utf-8 -*-
import scrapy
from datetime import date

class EdmjnlSpider(scrapy.Spider):
    name = 'news_edmjnl_crawl'
    start_urls = ['https://edmontonjournal.com/category/business']

    def parse(self, response):
        quotes = response.xpath('//*[@class="article-card__headline-clamp"]')
        
        for quote in quotes:
            yield {
                  'title': quote.xpath('.//text()').getall(),
                  'date': str(date.today()),
                  'source':'Edmonton_Journal',
                  'link': 'na',
            }