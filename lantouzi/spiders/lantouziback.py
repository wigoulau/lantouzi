# -*- coding: utf-8 -*-
import scrapy
import re
from lantouzi.items import LantouziItem

class LantouzibackSpider(scrapy.Spider):
    name = 'lantouziback'
    allowed_domains = ['lantouzi.com']
    start_urls = ['https://lantouzi.com/post?page=1']

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
            if (title.find('项目回款公告') >= 0):
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
        #print(response.url)
        item_nodes = response.css('.MsoNormal')
        for item_node in item_nodes:
            content = item_node.css('::text').extract_first()
            #print(content)
            pattern = re.compile('至(.*?)年(.*?)月(.*?)日.*退出(.*?)笔.*共(.*?)元')
            if (content.find("总计完成标的还款") >= 0):
                item = LantouziItem()
                result = pattern.findall(content)
                #print(result)
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
