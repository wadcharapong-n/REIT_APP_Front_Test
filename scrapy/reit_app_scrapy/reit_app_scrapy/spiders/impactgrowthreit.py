import scrapy
import json
from reit_app_scrapy.items import ImpactScrapyItem


class ImpactgrowthreitSpider(scrapy.Spider):
    name = "impactgrowthreit"
    start_urls = [
        'http://www.impactgrowthreit.com/about-impact-growth-reit/reit-information/?lang=th',
    ]

    def parse(self, response):

        # information = []
   
        find_strong = response.css('strong::text').extract()
        find_td = response.css('tr td::text').extract()
        item  = ImpactScrapyItem()
    
        item['reit_type'] = find_td[22].replace("\xa0","")
        item['investment_policy'] = find_td[23].replace("\xa0","")
        item['investment'] = find_td[24].replace("\xa0","")
        item['assets'] = find_td[25].replace("\xa0","")
        item['listed_unit'] = find_td[26].replace("\xa0","")
        item['ownership'] = find_td[27].replace("\xa0","")
        item['listed_date'] = find_td[28].replace("\xa0","")
        item['par_value'] = find_td[29].replace("\xa0","")
        item['dividend_policy'] = find_td[30].replace("\xa0","")

        yield item 


        # information.append({ "title" : find_strong[0].replace("\xa0","") , "content" : find_td[22].replace("\xa0","") })
        # information.append({ "title" : find_strong[1].replace("\xa0","") , "content" : find_td[23].replace("\xa0","") })
        # information.append({ "title" : find_strong[2].replace("\xa0","") , "content" : find_td[24].replace("\xa0","") })
        # information.append({ "title" : find_strong[3].replace("\xa0","") , "content" : find_td[25].replace("\xa0","") })
        # information.append({ "title" : find_strong[4].replace("\xa0","") , "content" : find_td[26].replace("\xa0","") })
        # information.append({ "title" : find_strong[5].replace("\xa0","") , "content" : find_td[27].replace("\xa0","") })
        # information.append({ "title" : find_strong[6].replace("\xa0","") , "content" : find_td[28].replace("\xa0","") })
        # information.append({ "title" : find_strong[7].replace("\xa0","") , "content" : find_td[29].replace("\xa0","") })
        # information.append({ "title" : find_strong[8].replace("\xa0","") , "content" : find_td[30].replace("\xa0","") })
       
        # information.append({ "title" : find_td[33].replace("\xa0","") , "content" : find_td[34].replace("\xa0","") })
        # information.append({ "title" : find_td[35].replace("\xa0","") , "content" : find_td[36].replace("\xa0","") })
        # information.append({ "title" : find_td[37].replace("\xa0","") , "content" : find_td[38].replace("\xa0","") })
        # information.append({ "title" : find_td[39].replace("\xa0","") , "content" : find_td[40].replace("\xa0","") })
        # information.append({ "title" : find_td[41].replace("\xa0","") , "content" : find_td[42].replace("\xa0","") })

        # for result in information:
        #      yield {
        #         'title': result['title'],
        #         'content': result['content'],
        #     }

    

            