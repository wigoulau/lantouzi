# -*- coding: utf-8 -*-
import scrapy
import re
from lantouzi.items import LantouziItem

class LantouzibackSpider(scrapy.Spider):
    name = 'lantouziback'
    allowed_domains = ['lantouzi.com']
    start_urls = ['https://lantouzi.com/post?page=26']

    def parse(self, response):
        print(response.url)
        page = int(response.url.split('=')[-1])  # 爬取页码
        item_nodes = response.css('.news-list li')
        for item_node in item_nodes:
            #print(item_node)
            #print(item_node.css('span::text').extract_first())
            title = item_node.css('a::text').extract_first()
            link = item_node.css('a::attr(href)').extract_first()
            #print(link)
            if (title.find('项目回款') >= 0):
                yield scrapy.Request(url=link, callback=self.parseContent)

        if item_nodes:
            next_page = page + 1
            next_url = response.url.replace("page={0}".format(page), "page={0}".format(next_page))
            yield scrapy.Request(url=next_url, callback=self.parse)

    def NumberStr(self, number):
        num = number.replace(',', '')
        num = num.replace('.', '')
        return num

    def parseContent(self, response):
        print(response.url)
        content = ""
        result = []
        item_nodes = response.css('.MsoNormal')

        for item_node in item_nodes:
            print(item_node.css('::text'))
            content = content + item_node.css('::text').extract_first()
        print(content)
        pattern1 = re.compile('至(.*)年(.*)月(.*)日.*退出(\d+)笔，共(.*?)元', flags=re.S)
        result1 = pattern1.findall(content)

        pattern2 = re.compile('至(.*)年(.*)月(.*)日.*还款(\d+)笔，共(.*?)元', flags=re.S)
        result2 = pattern2.findall(content)

        if (len(result1) > 0):
            result = result1
        if (len(result2) > 0):
            result = result2
        print(result)
        if (len(result) > 0):
            item = LantouziItem()
            year = result[0][0]
            month = result[0][1]
            day = result[0][2]
            count = self.NumberStr(result[0][3])
            money = self.NumberStr(result[0][4])
            item['year'] = year
            item['month'] = month
            item['day'] = day
            item['count'] = count
            item['money'] = money
            #print('add item')
            yield item
        #print('#####')
