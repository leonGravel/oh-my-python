# -*- coding: utf-8 -*-

# Scrapy settings for job_analyser project

BOT_NAME = 'job_analyser'

SPIDER_MODULES = ['job_analyser.spiders']
NEWSPIDER_MODULE = 'job_analyser.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

RANDOM_UA_TYPE = 'random'##random    chrome
DOWNLOADER_MIDDLEWARES = {
   'job_analyser.middlewares.JobAnalyserDownloaderMiddleware': 543,
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

# 修改编码为utf-8
FEED_EXPORT_ENCODING = 'utf-8'
DOWNLOAD_DELAY = 1

MYSQL_HOST = '132.232.103.230'
MYSQL_DB = 'spider'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'TX4mysql!'
MYSQL_PORT = '3306'
MYSQL_CHARSET = 'uft8'

ITEM_PIPELINES = {
    'job_analyser.pipelines.JobAnalyserPipeline': 300,
}