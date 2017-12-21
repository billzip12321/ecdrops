# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class Ecdropsbrand(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    brandname = Field()
    brandlink = Field()

class Ecdropscategory(Item):
    categoryname = Field()
    categorylink = Field()

class Ecdropsproduct(Item):
    brand = Field()
    category = Field()
    name = Field()
    price = Field()
    weight = Field()
    img = Field()
    size = Field()


