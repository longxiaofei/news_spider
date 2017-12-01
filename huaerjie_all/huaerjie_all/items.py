# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
	title = scrapy.Field()
	author = scrapy.Field()
	posted_time = scrapy.Field()
	comment_count = scrapy.Field()
	remark = scrapy.Field()
	content = scrapy.Field()
	source = scrapy.Field()
	url = scrapy.Field()
	crawl_time = scrapy.Field()
	id_ = scrapy.Field()
