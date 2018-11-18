# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
#负责数据清理并进行数据入库
class NovelspiderPipeline(object):
    def open_spider(self,spider):
        self.con = sqlite3.connect("../data.sqlite")
        self.cu = self.con.cursor()
        
    def process_item(self, item, spider):
#        print('pipeline')
#        print(spider.name)
        insert_sql = "insert into novel (title,author,detail) values('{}','{}','{}')".format(item['title'],item['author'],item['detail'])
        print(insert_sql)
        self.cu.execute(insert_sql)
        self.con.commit()
        return item
    
    def spider_close(self,spider):
        self.con.close()