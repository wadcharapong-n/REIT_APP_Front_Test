# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from reit_app_scrapy.items import ReitAppScrapyItem


class GvreitSpider(scrapy.Spider):
    name = 'gvreit'
    allowed_domains = ['www.gvreit.com']
    start_urls = ['http://www.gvreit.com/th/about_gvreit/about']

    def parse(self, response):
        item = ReitAppScrapyItem()
        item['trust_name_th'] = self.getData(response, '1', '2')
        item['trust_name_en'] = self.getData(response, '2', '2')
        item['ticker'] = self.getData(response, '3', '2')
        item['trustee'] = self.getData(response, '6', '2')
        item['address'] = ''
        item['investment_amount'] = self.getData(response, '10', '2')
        item['establishment_date'] = ''
        item['registration_date'] = ''
        item['reit_manager'] = self.getData(response, '4', '2')

        yield item

    def getData(self, response, valueTr, valueTd):
        value = response.css(
            'tr:nth-child('+valueTr+') td:nth-child('+valueTd+')::text').get()

        return value
