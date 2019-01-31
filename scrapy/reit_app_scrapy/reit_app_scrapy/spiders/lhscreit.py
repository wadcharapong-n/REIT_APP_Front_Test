# -*- coding: utf-8 -*-
import scrapy
import json
from reit_app_scrapy.items import ReitAppScrapyItem


class QuotesSpider(scrapy.Spider):
    name = "lhscreit"
    start_urls = [
        'https://www.lhscreit.com/overview',
    ]

    def parse(self, response):
        td = response.css("td::text").extract()
        item = ReitAppScrapyItem()

        item['trust_name_th'] = td[1]

        item['trust_name_en'] = td[3]

        item['ticker'] = td[5]

        item['trustee'] = td[41]

        item['address'] = "non-address"

        item['investment_amount'] = td[18]

        item['establishment_date'] = td[14]

        item['registration_date'] = td[16]

        item['reit_manager'] = td[37]

        yield item
    
