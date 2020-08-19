# -*- coding: utf-8 -*-
import scrapy
from datetime import date

class PostSpider(scrapy.Spider):
    name = 'post_crawl'
    start_urls = ['https://financialpost.com']

    def parse(self, response):
        quotes = response.xpath('//*[@class="article-card__headline-clamp"]')
        
        for quote in quotes:
            yield {
                  'title': quote.xpath('.//text()').get(),
                  'date': str(date.today()),
                  'source':'National_Post',
                  'link' : response.urljoin(quote.xpath('.//parent::h2/parent::a/@href').get()),
            }