# This file consists of the script to crawl the website
# http://www.yoga-centers-directory.net/nepal.htm
# and extract the required data
# The data can be extracted using the command:
# scrapy crawl yoga_centres
# The extracted data can be saved in the json file using the command:
# scrapy crawl yoga_centres -o yoga_centres.json

import scrapy

from scrapysample.items import ScrapysampleItem


class ScrapysampleSpider(scrapy.Spider):

    name = "yoga_centres"
    domain = "http://www.yoga-centers-directory.net/"
    start_urls = ["http://www.yoga-centers-directory.net/nepal.htm"]

    def parse(self, response):

        for sel in response.xpath('//div[@class="peach"]'):
            name = sel.xpath(
                'table/tr/td[@class="name_blank"]/a/text()').extract()
            tr_list = sel.xpath('table/tr')
            if not name:
                continue
            temp_dict = {
                'Address:': None,
                'Contact:': None,
                'Website:': None,
                'Instructor:': None,
                'Yoga Style:': None,
                'Description:': None
            }

            for items in tr_list:
                title = items.xpath('td[@class="orange"]/text()').extract()
                if not title:
                    continue
                value = items.xpath(
                    'td[@class="main"]/text()').extract()
                if value:
                    temp_dict[title[0]] = value

            scrapy_sample = ScrapysampleItem()
            scrapy_sample['name'] = name
            scrapy_sample['address'] = temp_dict['Address:']
            scrapy_sample['contact'] = temp_dict['Contact:']
            scrapy_sample['website'] = temp_dict['Website:']
            scrapy_sample['instructor'] = temp_dict['Instructor:']
            scrapy_sample['yoga_style'] = temp_dict['Yoga Style:']
            scrapy_sample['description'] = temp_dict['Description:']
            yield scrapy_sample
