# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobAnalyserItem(scrapy.Item):
    # define the fields for your item here like:
    job_title = scrapy.Field()
    salary = scrapy.Field()
    company_name = scrapy.Field()
    job_desc = scrapy.Field()
    pass


class NoticeItem(scrapy.Item):
    # define the fields for your item here like:
    notice_title = scrapy.Field()
    notice_time = scrapy.Field()
    publisher = scrapy.Field()
    content = scrapy.Field()
    pass