# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EastfundsspiderItem(scrapy.Item):
    #基本信息
    fundname=scrapy.Field()
    fundid=scrapy.Field()
    fundtype=scrapy.Field()
    fundcompany=scrapy.Field()
    fundsize=scrapy.Field()

    #nav
    todayestnav=scrapy.Field()
    yestnav=scrapy.Field()
    accumnav=scrapy.Field()

    #收益率
    weekrate=scrapy.Field()
    monthrate=scrapy.Field()
    threemonthrate=scrapy.Field()
    sixmonthrate=scrapy.Field()
    fromthisyearrate=scrapy.Field()
    yearrate=scrapy.Field()
    twoyearrate=scrapy.Field()
    threeyearrate=scrapy.Field()

    #industry
    industry1=scrapy.Field()
    industry1ratio=scrapy.Field()
    industry2=scrapy.Field()
    industry2ratio=scrapy.Field()

    category=scrapy.Field() #净值、万份收益
    date=scrapy.Field()#当日日期
