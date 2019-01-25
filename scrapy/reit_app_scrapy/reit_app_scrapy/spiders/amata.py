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
        item['authorized_capital'] = self.getDataByIndex(response,'4')
        item['paid_up_capital'] = self.getDataByIndex(response,'5')
        item['par_value'] = self.getDataByIndex(response,'6')
        item['duration_of_trust'] = self.getDataByIndex(response,'7')
        item['type_of_trust'] = self.getDataByIndex(response,'8')
        item['trustee'] = self.getDataByIndex(response,'9')
        item['address_trustee'] = self.getDataByIndex(response,'10')
        item['type_of_business'] = self.getDataByIndex(response,'11')
        item['auditor'] = self.getDataByIndex(response,'12')
        yield item  

    def getDataByIndex(self,response,valueIndex):
        value = Selector(response).xpath('//*[@id="main"]/div/table/tbody/tr['+valueIndex+']/td[2]/text()').extract()[0]
        return value
    
        
