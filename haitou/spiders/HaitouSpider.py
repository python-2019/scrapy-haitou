# -*- coding: utf-8 -*-
import scrapy

from haitou.items import HaitouItem


class HaitouSpider(scrapy.Spider):
    name = 'haitou'
    allowed_domains = ['xjh.haitou.cc']
    host = "https://xjh.haitou.cc"
    now_page_pre = "/page-"
    now_page = 1
    city_pre = "/"
    start_urls = [host]

    def parse(self, response):
        city_list = response.xpath(
            "//div[@class='dropdown-menu dropdown-menu-ht animated fadeInUp dropdown-city']/a/@data-value").extract()
        for city in city_list:
            # 根据页面规律 组合url
            url = self.host + self.city_pre + city + self.now_page_pre + str(self.now_page)
            yield scrapy.Request(url, callback=self.parse_list)

    def parse_list(self, response):
        """
            爬取list以及分页
        """
        print(response.url)
        tr_list = response.xpath("//tr[@data-source='xjh']")
        for tr in tr_list:
            item = HaitouItem()
            item['company'] = tr.xpath("./td[2]/a/div/text()").extract_first()
            item['school'] = tr.xpath("./td[2]/a/@title").extract_first()
            item['holding_time'] = tr.xpath("./td[3]/span[1]/text()").extract_first()
            item['addr'] = tr.xpath("./td[4]/span[1]/text()").extract_first()
            item['href'] = self.host + tr.xpath("./td[7]/a/@href").extract_first()
            yield item
        # 翻页
        next_page = response.xpath("//a[contains(text(),'›')]/@href").extract_first()
        if next_page is not None:
            next_page_url = self.host + next_page
            print(next_page_url)
            yield scrapy.Request(
                next_page_url,
                callback=self.parse_list
            )
