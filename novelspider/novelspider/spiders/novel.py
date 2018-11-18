# -*- coding: utf-8 -*-
import scrapy
from ..items import NovelspiderItem

class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['http://www.quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com/list/1_1.html','http://www.quanshuwang.com/list/1_2.html']

    def parse(self, response):
        item = NovelspiderItem()
        title = response.xpath('//*[@id="navList"]/section/ul//li/span/a[1]/text()').extract()
        author = response.xpath('//*[@id="navList"]/section/ul//li/span/a[2]/text()').extract()
        detail = response.xpath('//*[@id="navList"]/section/ul//li/span/em/text()').extract()
        for i in range(len(title)):
#            print(title[i],author[i],detail[i])
            item['title'] = title[i]
            item['author'] = author[i]
            item['detail'] = detail[i]
            yield item
#        pass
