# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EastfundsspiderItem(scrapy.Item):
    fundname=scrapy.Field()
    fundid=scrapy.Field()
    todayestnav=scrapy.Field()
    yestnav=scrapy.Field()
    accumnav=scrapy.Field()
    category=scrapy.Field()
    date=scrapy.Field()
    weekrate=scrapy.Field()
    monthrate=scrapy.Field()
    threemonthrate=scrapy.Field()
    sixmonthrate=scrapy.Field()
    fromthisyearrate=scrapy.Field()
    yearrate=scrapy.Field()
    twoyearrate=scrapy.Field()
    threeyearrate=scrapy.Field()



