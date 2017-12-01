# -*- coding: utf-8 -*-

BOT_NAME = 'huaerjie_all'

SPIDER_MODULES = ['huaerjie_all.spiders']
NEWSPIDER_MODULE = 'huaerjie_all.spiders'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 32

DOWNLOAD_DELAY = 0.2

DOWNLOAD_TIMEOUT = 5

COOKIES_ENABLED = False

RETRY_ENABLED = True
RETRY_TIMES = 3

LOG_LEVEL = 'INFO'

# redis爬取队列设置
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# SCHEDULER_PERSIST = True
# REDIS_HOST = 'localhost'
# REDIS_PORT = 6379

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.8',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Referer': 'https://wallstreetcn.com/',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}


# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   #'huaerjie_all.middlewares.TestMiddleware': 543,
}


ITEM_PIPELINES = {
   'huaerjie_all.pipelines.HuaerjieAllPipeline': 1,
   #'huaerjie_all.pipelines.ElasticSearchPipeline': 2,
}


MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'test'
MYSQL_USER = 'root'
MYSQL_PWD = 'root'


