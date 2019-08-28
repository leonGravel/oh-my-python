# -*- coding: utf-8 -*-
import scrapy
from job_analyser.items import JobAnalyserItem
from scrapy.selector import HtmlXPathSelector


class BossSpider(scrapy.Spider):
    name = 'BossSpider'

    start_urls = [
        'https://www.zhipin.com/c101040100/?query=产品经理&page=1',
    ]

    def  get_job_info(self, response):
        hxs = HtmlXPathSelector(response)
        item = response.meta['item']
        items = []
        content = hxs.select('//div[@class="job-sec"]/div[@class="text"]/text()').extract()

        item['job_desc'] = content
        items.append(item)
        return items

    def parse(self, response):
        base_url = 'https://www.zhipin.com/'
        for quote in response.xpath('//div[@class="job-primary"]'):
            item = JobAnalyserItem()
            item['job_title'] = quote.xpath('.//div[@class="job-title"]/text()').extract_first()
            item['salary'] = quote.xpath('.//span[@class="red"]/text()').extract_first()
            item['company_name'] = quote.xpath(
                './/div[@class="info-company"]/div[@class="company-text"]/h3/a/text()').extract_first()
            target_url = base_url + quote.xpath(
                './/div[@class="info-primary"]/h3[@class="name"]/a/@href').extract_first()
            yield scrapy.Request(target_url, meta={'item': item}, callback=self.get_job_info)

        next_page_url = base_url + response.xpath('//div[@class="page"]/a[@class="next"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
