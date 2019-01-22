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
            self.checkDuplicate(item, spider)
        else:
            log.msg("REIT duplicate in MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item

    def checkDuplicate(self, item, spider):

        # print('Check Collecttion')
        check_collection = self.collection.find({}, {"_id": 0}).count()
        if check_collection == 0:
            # print('Insert Collecttion')
            self.collection.insert(dict(item))
            log.msg("REIT added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
            return False

        # print('Check Contain')
        item_db = self.collection.find()
        for data in item_db:
            for key in data:
                if key != '_id':
                    if data[key] != item[key]:
                        myquery = {key: data[key]}
                        newvalues = {"$set": {key: item[key]}}
                        self.collection.update_one(myquery, newvalues)
                        # print('Update Collection')

        log.msg("REIT updated to MongoDB database!",
                level=log.DEBUG, spider=spider)

        return False
