# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class ReitAppScrapyPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            if self.checkDuplicate(item):
                self.collection.insert(dict(item))
                log.msg("REIT added to MongoDB database!",
                        level=log.DEBUG, spider=spider)
            else:
                log.msg("REIT duplicate in MongoDB database!",
                        level=log.DEBUG, spider=spider)
        return item

    def checkDuplicate(self, item):
        # print "************** : " + item['name']
        doc = self.collection.find()
        for d in doc:
            if d['name'] ==  item['name']:
                # print "************ Diplicate **************"
                return False
        
        # print "************ Not Diplicate **************"
        return True
