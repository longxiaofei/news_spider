# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
from MySQLdb import cursors
from twisted.enterprise import adbapi
from huaerjie_all.es_models import ArticleType

class HuaerjieAllPipeline(object):

	def __init__(self, dbpool):
		self.dbpool = dbpool
		self.insert_sql = """
			insert into hej(id, title, author, posted_time, comment_count, remark, content, source, url)
			VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
		"""

	@classmethod
	def from_crawler(cls, crawler):
		dbparms = dict(
			host = crawler.settings['MYSQL_HOST'],
			user = crawler.settings['MYSQL_USER'],
			passwd = crawler.settings['MYSQL_PWD'],
			db = crawler.settings['MYSQL_DBNAME'],
			charset = 'utf8',
			cursorclass = cursors.DictCursor,
			use_unicode = True,
		)
		dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

		return cls(dbpool)

	def process_item(self, item, spider):

		query = self.dbpool.runInteraction(self.db_insert, item)
		query.addErrback(self.handle_error, item, spider)

		return item

	def handle_error(self, failure, item, spider):
		print(failure, spider.name)

	def db_insert(self, cursor, item):

		if item['title'] and item['content']:
			params = (
				item['id_'],
				item['title'],
				item['author'],
				item['posted_time'],
				item['comment_count'],
				item['remark'],
				item['content'],
				item['source'],
				item['url']
			)
			cursor.execute(self.insert_sql, params)




