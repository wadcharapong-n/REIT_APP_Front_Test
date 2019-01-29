# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from reit_app_scrapy.items import ReitAppScrapyItem

class AmataSpider(scrapy.Spider):
    name = 'amata'
    allowed_domains = ['www.amatareit.com']
    start_urls = ['http://www.amatareit.com/trust_information.html']

 
    def parse(self, response):
        item = ReitAppScrapyItem()
        item['trust_name_th'] = self.getDataByIndex(response,'1')
        item['trust_name_en'] = self.getDataByIndex(response,'2')
        item['ticker'] = self.getDataByIndex(response,'3')
        item['investment_amount'] = self.getDataByIndex(response,'5')
        item['trustee'] = self.getDataByIndex(response,'9')
        item['address'] = self.getDataByIndex(response,'10')
        yield item  

    def getDataByIndex(self,response,valueIndex):
        value = Selector(response).xpath('//*[@id="main"]/div/table/tbody/tr['+valueIndex+']/td[2]/text()').extract()[0]
        return value
    
        
