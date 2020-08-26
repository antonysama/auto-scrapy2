import scrapy
from datetime import date

class CgySpider(scrapy.Spider):
    name = 'cgy_crawl'
    start_urls = ['https://calgaryherald.com/category/business']

    def parse(self, response):
        quotes = response.xpath('//*[@class="article-card__headline-clamp"]')
        
        for quote in quotes:
            yield {
                  'title': quote.xpath('.//text()').getall(),
                  'date': str(date.today()),
                  'source':'Calgary_Herald',
                  'link': response.urljoin(quote.xpath('.//parent::h2/parent::a/@href').get()),
            }
