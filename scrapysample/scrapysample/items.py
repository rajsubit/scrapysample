# The items to be extracted from the website
# http://www.yoga-centers-directory.net/nepal.htm
# are defined here

import scrapy


class ScrapysampleItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    contact = scrapy.Field()
    website = scrapy.Field()
    instructor = scrapy.Field()
    yoga_style = scrapy.Field()
    description = scrapy.Field()
