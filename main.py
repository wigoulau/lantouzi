from scrapy.cmdline import execute
#执行命令行命令scrapy crawl lantouziback -o items.json
execute(["scrapy", "crawl", "lantouziback", "-o", "items.csv", "--nolog"])