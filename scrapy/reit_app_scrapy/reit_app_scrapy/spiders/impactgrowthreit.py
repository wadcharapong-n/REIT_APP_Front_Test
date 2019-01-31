import scrapy
import json
from reit_app_scrapy.items import ReitAppScrapyItem


class ImpactgrowthreitSpider(scrapy.Spider):
    name = "impactgrowthreit"
    start_urls = [
        'http://www.impactgrowthreit.com/about-impact-growth-reit/reit-information/?lang=th',
    ]

    def parse(self, response):

        find_td = response.css('tr td::text').extract()
        find_trust_name = response.css('p span strong span::text').extract()
        item  = ReitAppScrapyItem()
      
        # item['trust_name_th'] = find_trust_name[0]
        # item['reit_type'] = find_td[22]
        # item['investment_policy'] = find_td[23]
        # item['investment'] = find_td[24]
        # item['listed_unit'] = find_td[26]
        # item['ownership'] = find_td[27]
        # item['listed_date'] = find_td[28]
        # item['par_value'] = find_td[29]
        # item['dividend_policy'] = find_td[30]


        item['trust_name_th'] = find_trust_name[0].encode(
            'utf8').replace('\xe2\x80\x93 FACT SHEET', "").decode(
            'utf8')
        item['ticker'] = 'IMPACT'
        item['trustee'] = ''
        item['address'] = ''
        item['investment_amount'] = find_td[23]
        item['establishment_date'] = ''
        item['registration_date'] = ''
        item['reit_manager'] = ''
                    
        yield item 


        
       

    