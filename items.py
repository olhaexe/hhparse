# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

def title_string(words):
    string = ''
    for word in words:
        string += word
    return string

def salary_string(words):
    string = ''
    for word in words:
        string += word
    return string

class HeadhunterItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field(input_processor=MapCompose(title_string), output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    salary = scrapy.Field(input_processor=MapCompose(title_string), output_processor=salary_string)
    skills = scrapy.Field()
    enterprise = scrapy.Field(output_processor=TakeFirst())
    enterprise_url = scrapy.Field(output_processor=TakeFirst())
    enterprise_logo = scrapy.Field(output_processor=TakeFirst())
