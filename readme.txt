# 获取懒投资回款情况
1. scrapy startproject lantouzi
2. scrapy genspider lantouziback lantouzi.com
3. scrapy crawl lantouziback -o items.json