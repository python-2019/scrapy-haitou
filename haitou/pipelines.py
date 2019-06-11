# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import time

from scrapy.conf import settings
import logging
import os


class HaitouPipeline(object):

    def open_spider(self, spider):
        file_path = settings.get("FILE_PATH")
        if os.path.exists(file_path):
            os.rename(file_path, file_path.replace('.csv', "_" + str(time.time()) + '.csv'))
        self.file = open(file_path, 'a', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.file)
        headers = ['公司', '学校', '举办时间', '地点', '详情']
        self.csv_writer.writerow(headers)

    def process_item(self, item, spider):
        item['holding_time'] = item['holding_time']
        item['school'] = item['school'][item['school'].find("学校：") + 3:item['school'].find("地点：") - 1]
        row = [item['company'], item['school'], item['holding_time'], item['addr'], item['href']]
        self.csv_writer.writerow(row)
        print(row)
        return item

    def close_spider(self, spider):
        try:
            self.file.closed()
        except Exception:
            logging.warning("\n\n======爬取完毕=====")
