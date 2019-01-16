# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class LalinSpider(scrapy.Spider):
    name = 'lalin'
    allowed_domains = ['lalinproperty.com']
    start_urls = ['http://lalinproperty.com/lalin-profile/']

    def parse(self, response):
        data = Selector(response).xpath('/html/body/div[2]/div/div/section/div/div/div/div/div/div[2]/div/div/div[2]/div[1]/p').extract()[0]
        # print data
        dataArr = data.split('<br>')
        for d in dataArr:
            value = d.split('</strong>')
            yield {'value is :: ' :value[1] }
        # for question in questions:
        #     item = StackItem()
        #     item['title'] = question.xpath(
        #         'a[@class="question-hyperlink"]/text()').extract()[0]
        #     item['url'] = question.xpath(
        #         'a[@class="question-hyperlink"]/@href').extract()[0]
        #     yield item
