# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HaitouItem(scrapy.Item):
    """
        海投网宣讲会item
    """
    # 公司
    company = scrapy.Field()
    # 学校
    school = scrapy.Field()
    # 举办时间
    holding_time = scrapy.Field()
    # 地点
    addr = scrapy.Field()
    # 详情
    href = scrapy.Field()