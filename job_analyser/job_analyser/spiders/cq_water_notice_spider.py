# -*- coding: utf-8 -*-
import scrapy
from job_analyser.items import NoticeItem
from scrapy.selector import HtmlXPathSelector


class WaterNoticeSpider(scrapy.Spider):
    name = 'cqwnSpider'

    start_urls = [
        'http://www.cq966886.com/wsfw.php?cid=49&page=1',
    ]

    def  get_title_info(self, response):
        hxs = HtmlXPathSelector(response)
        item = response.meta['item']
        items = []
        item['content'] = hxs.select('//td[@class="content_line"]').xpath('string(.)').extract()
        items.append(item)
        return items

    def parse(self, response):
        base_url = 'http://www.cq966886.com/'
        for quote in response.xpath('//td[@class="list2"]/..'):
            item = NoticeItem()
            item['notice_title'] = quote.xpath('.//td[@class="list2"]/a/b/text()').extract_first()
            item['notice_time'] = quote.xpath('.//td[@class="text3"]/text()').extract_first()

            target_url = base_url + quote.xpath('.//td[@class="list2"]/a/@href').extract_first()
            yield scrapy.Request(target_url, meta={'item': item}, callback=self.get_title_info)

        next_page_url = base_url + response.xpath('//a[contains(text(),"下一页")]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
