# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.pipelines.images import ImagesPipeline
#scrapy genspider -t crawl doutu www.doutula.com
class DoutuSpider(CrawlSpider):
    name = 'doutu'
    allowed_domains = ['doutula.com']
    start_urls = ['http://www.doutula.com/']

#分析http://www.doutula.com/的相应，提取全部url，符合规则继续请求，拿到相应交给回调函数
#follow为true时，还会提取相应中的url，在进行分析，在进行提取和匹配规则，直到匹配不到或者匹配到重复的
    rules = (
#        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'http://www.doutula.com/article/detail/\d+'), callback='parse_item', follow=False),
    )
    
    
    
#回调 callback='parse_item'
    def parse_item(self, response):
        i = {}
        i["image_urls"] = []
        i["images"] = []
        
#        img_urls = response.xpath('规则').extract()
#        img_urls = response.xpath('.//div[@class="pic-content"]//img/@src').extract()
        i["image_urls"] = response.xpath('.//div[@class="pic-content"]//img/@src').extract()
#        print(img_urls)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
