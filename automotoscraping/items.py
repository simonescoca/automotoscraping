# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AutomotoBrand(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    pass

class AutomotoModel(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    pass

class AutomotoVersion(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    pass