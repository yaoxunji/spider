# -*- coding: utf-8 -*-
import scrapy

#scrapy genspider sp www.test.com 
class SpSpider(scrapy.Spider):
    name = 'sp'
    allowed_domains = ['www.test.com']
    start_urls = ['http://www.test.com/']

    def parse(self, response):
        pass
