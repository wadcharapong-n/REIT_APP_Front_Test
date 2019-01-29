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
    trust_name_th = Field() #ชิื่อกองTH
    trust_name_en = Field() #ชิื่อกองEN
    ticker = Field() #ชื่อย่อ
    trustee = Field() #ทรัสตี้
    address = Field() #ที่อยู่
    investment_amount = Field() #ทุนจดทะเบียน
    establishment_date = Field() #วันจัดตั้งกองทุน
    registration_date = Field() #วันจดทะเบียน
    reit_manager = Field() #ผู้บริหาร REIT

# class ImpactScrapyItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     trust_name_th = Field()
#     reit_type = Field()
#     investment_policy = Field()
#     investment = Field()
#     assets = Field()
#     listed_unit = Field()
#     ownership = Field()
#     listed_date = Field()
#     par_value = Field()
#     dividend_policy = Field()

# class ReitLhscAppScrapyItem(scrapy.Item):
#     trust_name_th = Field()
#     establishment_date = Field()
#     registration_date = Field()
#     reit_manager = Field()
#     trust_tee = Field()
#     property_manager = Field()
#     investment_amount = Field()
#     investment_unit_amount = Field()
#     loan_amount = Field()
#     per_original_owner = Field()
#     per_general_public = Field()

