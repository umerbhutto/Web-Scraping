# -*- coding: utf-8 -*-
import scrapy


class CraiglistSpiderMultipleSpider(scrapy.Spider):
    name = 'craiglist_spider_multiple'
    allowed_domains = ["newyork.craiglist.org"]
    start_urls = ['https://newyork.craigslist.org/d/jobs/search/jjj/']

    def parse(self,response):
        
        listings = response.xpath('//*[@class = "result-row"]')
        
        for listing in listings:
            date = listing.xpath('.//*[@class = "result-date"]/@datetime').extract_first()
            title = listing.xpath('.//*[@class = "result-title hdrlnk"]/text()').extract_first()                 
            place = listing.xpath('.//*[@class = "result-hood"]/text()').extract_first()
            link = listings.xpath('.//*[@class = "result-title hdrlnk"]/@href').extract_first()

            yield{
                'date':date,
                'title':title,
                'link':link,
                'place':place                
            }

            

