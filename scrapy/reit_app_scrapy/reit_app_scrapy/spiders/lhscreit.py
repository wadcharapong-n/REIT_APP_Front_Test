# -*- coding: utf-8 -*-
import scrapy
import json
# from reit_app_scrapy.items import ReitLhscAppScrapyItem

class QuotesSpider(scrapy.Spider):
    name = "lhscreit"
    start_urls = [
        'lhscreit.com/porthilight',
    ]

    def parse(self, response):

        # td = response.css("td::text").extract()
        # trustName = td[0]
        # establishmentDate = td[1]
        # registrationDate = td[2]
        # investmentValue = td[3]
        # investmentUnit = td[4]
        # loan = td[5]
        # originalOwner = td[6]
        # generalPublic = td[7]
        # reitManager = td[8]
        # trusTee = td[9]
        # propertyManager = td[10]
        # strong = response.css("strong::text").extract()
        # investmentAmount = strong[4]+strong[5]
        # investmentUnitAmount = strong[6]
        # loanAmount = strong[7]
        # perOriginalOwner = strong[10]
        # perGeneralPublic = strong[11]

        # item = ReitLhscAppScrapyItem()
        # item['trust_name_th'] = td[0]
        # item['establishment_date'] = td[1]
        # item['registration_date'] = td[2]
        # item['reit_manager'] = td[8]
        # item['trust_tee'] = td[9]
        # item['property_manager'] = td[10]
        # item['investment_amount'] = strong[4]+strong[5]
        # item['investment_unit_amount'] = strong[6]
        # item['loan_amount'] = strong[7]
        # item['per_original_owner'] = strong[10]
        # item['per_general_public'] = strong[11]
