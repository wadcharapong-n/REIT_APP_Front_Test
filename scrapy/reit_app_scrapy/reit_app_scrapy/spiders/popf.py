# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from reit_app_scrapy.items import ReitAppScrapyItem

class PopfSpider(scrapy.Spider):
    name = 'popf'
    allowed_domains = ['www.popf-fund.com']
    start_urls = ['http://www.popf-fund.com/about/fund_information']

 
    def parse(self, response):
        
        item = ReitAppScrapyItem()
        
        td = response.css("td::text").extract()
        p = response.css("p::text").extract()
        # item['trust_name_th'] = self.getDataByIndex(response,'1','1','0','0')
        # item['trust_name_en'] = self.getDataByIndex(response,'1','2','0','0')
        # item['ticker'] = self.getDataByIndex(response,'1','3','0','0')
        # item['trustee'] = self.getDataByIndex(response,'0','0','4','0')
        # item['address'] = self.getDataByIndex(response,'3','1','0','1')+self.getDataByIndex(response,'3','1','0','2')
        # item['investment_amount'] = self.getDataByIndex(response,'1','3','0','0')
        # item['establishment_date'] = "22 มีนาคม 2554"
        # item['registration_date'] = "31 มีนาคม 2554"
        # item['reit_manager'] = self.getDataByIndex(response,'0','0','1','0')

        item['trust_name_th'] = td[2]
        item['trust_name_en'] = td[5]
        item['ticker'] = td[8]
        item['trustee'] = p[19]
        item['address'] = "non-address"
        item['investment_amount'] = td[25]
        item['establishment_date'] = "22 มีนาคม 2554"
        item['registration_date'] = "31 มีนาคม 2554"
        item['reit_manager'] = p[11]

        yield item  


    # def getDataByIndex(self,response,tableIndex,trIndex,divIndex,textIndex):
    #     if divIndex == 0 and textIndex == 0:
    #         value = Selector(response).xpath('//*[@id="ir_content"]/table['+tableIndex+']/tbody/tr['+trIndex+']/td[3]/text()').extract()
    #     elif divIndex !=0:
    #         value = Selector(response).xpath('//*[@id="ir_content"]/div['+divIndex+']/p[1]//text()').extract()
    #     else :
    #         value = Selector(response).xpath('//*[@id="ir_content"]/table[3]/tbody/tr[1]/td[3]/text()['+textIndex+']').extract()
    #     return value



        
        