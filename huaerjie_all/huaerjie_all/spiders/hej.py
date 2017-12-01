# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from huaerjie_all.items import NewsItem
from datetime import datetime
from huaerjie_all.common import get_md5

class HejSpider(CrawlSpider):
    name = 'hej'
    allowed_domains = [
        'wallstreetcn.com', # 华尔街见闻
        'awtmt.com', # 全天候科技
        'goldtoutiao.com', # 黄金头条
    ]
    start_urls = [
        'http://wallstreetcn.com/',
        'https://goldtoutiao.com/news/gold-latest',
        'https://awtmt.com/',
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'https://wallstreetcn\.com/articles/\d*',)), callback='parse_hej', follow=True),
        Rule(LinkExtractor(allow=(r'https://goldtoutiao\.com/articles/\d*.*',)), callback='parse_goldtoutiao', follow=True),
        Rule(LinkExtractor(allow=(r'https://awtmt\.com/articles/\d*.*',)), callback='parse_awtmt', follow=True),
    )

    # 华尔街见闻
    def parse_hej(self, response):

        if not response.xpath('.//*[@class="layout-main"]').extract_first():
            return

        if 'premium' not in response.url and 'errMsg' not in response.url:
            url = response.url
            title = response.xpath('.//*[@class="article__heading__title"]/text()').extract_first()
            author = response.xpath('.//*[@class="user-card__row__name"]/text()').extract_first()
            if not author:
                author = response.xpath('.//*[@class="article__heading__meta__source"]/text()').extract_first()
            if not author:
                author = '华尔街见闻'
            author = author.replace('来源:\xa0', '')
            temp_group = response.xpath('.//*[@class="meta-item__text"]/text()').extract()
            posted_time = temp_group[0]
            posted_time = datetime.strptime(posted_time, '%Y-%m-%d %H:%M')
            try:
                comment_count = temp_group[1].replace('\n', '').replace(' ', '')
            except:
                comment_count = 0
            content = ''.join(response.xpath('.//*[@class="node-article-content"]//p//text()').extract()).replace('\xa0', '')
            remark = content[:100]
            source = '华尔街见闻'
            crawl_time = datetime.now()
            id_ = get_md5(url)

            item = NewsItem()
            for field in item.fields:
                item[field] = eval(field)
            yield item

    # 全天候科技
    def parse_awtmt(self, response):
        url = response.url
        title = response.xpath('.//*[@class="article-detail-title"]/text()').extract_first().replace('\n', '').replace(' ', '')
        author = response.xpath('.//*[@class="author-link"]/text()').extract_first()
        if not author:
            author = response.xpath('.//*[@class="article-source-name"]/text()').extract_first()
        if not author:
            author = '全天候科技'
        posted_time = response.xpath('.//*[@class="article-create-time"]/text()').extract_first()
        posted_time = datetime.strptime(posted_time, '发表于%Y年%m月%d日 %H:%M')
        comment_count = response.xpath('.//*[@class="article-comments-count"]/text()').extract_first().replace('条评论', '')
        remark = ''.join(response.xpath('.//*[@class="article-detail-summary"]//text()').extract()).replace('\n', '').replace(' ', '')
        content = ''.join(response.xpath('.//*[contains(@class, "article-detail-text")]//p/text()').extract()).replace('\xa0', '')
        source = '全天候科技'
        crawl_time = datetime.now()
        id_ = get_md5(url)

        item = NewsItem()
        for field in item.fields:
            item[field] = eval(field)
        yield item

    # 黄金头条
    def parse_goldtoutiao(self, response):
        url = response.url
        title = response.xpath('.//*[@class="article-title"]/text()').extract_first()
        author = response.xpath('.//*[@class="author-name"]/text()').extract_first().replace(' ', '')
        posted_time = response.xpath('.//*[@class="article-author-wrap"]/span/text()').extract_first().replace(' ', '').replace('·', '')
        posted_time = datetime.strptime(posted_time, '%Y年%m月%d日%H:%M:%S')
        comment_count = response.xpath('.//*[@class="article-comments-header"]/text()').extract_first().replace('条评论', '')
        remark = response.xpath('.//*[@class="article-summary"]//text()').extract_first()
        content = ''.join(response.xpath('.//*[contains(@class, "article-detail-content")]//p/text()').extract()).replace('\xa0', '')
        source = '黄金头条'
        crawl_time = datetime.now()
        id_ = get_md5(url)

        item = NewsItem()
        for field in item.fields:
            item[field] = eval(field)
        yield item