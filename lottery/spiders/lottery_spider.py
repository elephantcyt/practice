# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from lottery.items import LotteryItem

class LotterySpider(Spider):
    name = 'lottery_spider'
    allowed_domains = ['https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx']
    start_urls = ['https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx/']

    def parse(self, response):
        item = LotteryItem()
        number = response.xpath('//td[@class="td_w font_black14b_center"]/span/text()').extract()
        for i in range(10):
            item["dateterm"] = response.xpath('//td[@class="td_w"]/span[@id="SuperLotto638Control_history1_dlQuery_DrawTerm_%s"]/text()' % i).extract_first()
            item["date"] = response.xpath('//td[@class="td_w"]/span[@id="SuperLotto638Control_history1_dlQuery_Date_%s"]/text()' % i).extract_first()
            item["total"] = response.xpath('//td[@class="td_w"]/span[@id="SuperLotto638Control_history1_dlQuery_Total_%s"]/text()' % i).extract_first()
            item["number"] = number[12*i+0:12*i+6]
            item["special"] = response.xpath('//td[@colspan="2"]/span[@id="SuperLotto638Control_history1_dlQuery_No7_%s"]/text()' % i).extract_first()
            print (item["dateterm"])
            print (item["date"])
            print (item["total"])
            print (item["number"])
            yield {'dataterm' : item["dateterm"], 'date' : item["date"], 'total' : item["total"], "number" : item["number"], "special" : item["special"]}
