# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from reit_app_scrapy.items import ReitAppScrapyItem

class LalinSpider(scrapy.Spider):
    name = 'lalin'
    allowed_domains = ['lalinproperty.com']
    start_urls = ['http://lalinproperty.com/lalin-profile/']

    # def __init__(self, subURL=None, *args, **kwargs):
    #     super(LalinSpider, self).__init__(*args, **kwargs)
    #     self.start_urls = ['http://lalinproperty.com/%s' % subURL]
    # def start_requests(self):
    #     yield scrapy.Request('http://lalinproperty.com/%s' % self.subURL)

    def parse(self, response):
        data = Selector(response).xpath('/html/body/div[2]/div/div/section/div/div/div/div/div/div[2]/div/div/div[2]/div[1]/p').extract()[0]
        # print data
        dataArr = data.split('<br>')
        # for d in dataArr:
        #     value = d.split('</strong>')
        #     item = ReitAppScrapyItem()
        #     item['title'] = value[1]
        #     yield item
        item = ReitAppScrapyItem()
        value = dataArr[0].split('</strong>')
        item['name'] = value[1]
        value = dataArr[1].split('</strong>')
        item['catagory'] = value[1]
        value = dataArr[2].split('</strong>')
        item['identity_id'] = value[1]
        value = dataArr[3].split('</strong>')
        item['url'] = value[1]
        value = dataArr[10].split('</strong>')
        item['lead'] = value[1]
        yield item
