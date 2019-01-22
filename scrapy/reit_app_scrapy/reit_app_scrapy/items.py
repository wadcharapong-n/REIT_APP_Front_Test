# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.item import Item, Field

class ReitAppScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    trust_name_th = Field()
    trust_name_en = Field()
    ticker = Field()
    authorized_capital = Field()
    paid_up_capital = Field()
    par_value = Field()
    duration_of_trust = Field()
    type_of_trust = Field()
    trustee = Field()
    address_trustee = Field()
    type_of_business = Field()
    auditor = Field()

class ReitLhscAppScrapyItem(scrapy.Item):
    trust_name_th = Field()
    establishment_date = Field()
    registration_date = Field()
    reit_manager = Field()
    trust_tee = Field()
    property_manager = Field()
    investment_amount = Field()
    investment_unit_amount = Field()
    loan_amount = Field()
    per_original_owner = Field()
    per_general_public = Field()

