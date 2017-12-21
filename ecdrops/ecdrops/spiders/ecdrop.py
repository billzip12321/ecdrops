# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from ecdrops.items import Ecdropsproduct

class EcdropSpider(scrapy.Spider):
    name = 'ecdrop'
    allowed_domains = ['ecdrops.se']
    start_urls = ['http://ecdrops.se/']

    def parse(self, response):
        #for sel in response.css('.text-left'):
        #     item = Ecdropsbrand()
        #     item['brand']=sel.css('a::text').extract()
        #     item['brandlink']=sel.css('a::attr(href)').extract()
        #     yield item

        
        urls = response.css('.text-left a::attr(href)').extract()
        for url in urls:
        	self.log('Found brand url: %s' % url)
        	yield Request(url, callback = self.parseCategory)

    def parseCategory(self, response):

        links = response.xpath('//ul[@class="list-unstyled category-list"]/li/a/@href').extract()
        for link in links:
        	self.log('Found category link: %s' %link)
        	yield Request(link, callback =self.parseproduct)

    def parseproduct(self, response):
        
        #products = response.css('.col-xs-6')
        #for count, product in enumerate(products):
            #args= (count, product.css('.product-name::text').re(r'(.*)\n\s*'), product.css('.price-new::text').re(r'^\$\s(.*)'), product.css('option::attr(value)').extract(), product.css('a::attr(href)').extract())
            #print('%d, %s, %s, %s, %s' %args)  	
        for sel in response.css('.col-xs-6'):
        	item = Ecdropsproduct()
        	item['brand']=response.css('.text-center::text').extract_first()
        	item['category']=response.css('h2.text-center::text').re(r'\n\s*(.*)\n')[0]
        	item['name']=sel.css('.product-name::text').re(r'(.*)\n\s*')[0]
        	item['price']=sel.css('.price-new::text').re(r'^\$\s(.*)')[0]
        	item['weight']=sel.css('a::attr(title)').re(r'\((\d\.\d{2})\)')[0]
        	item['size']=sel.css('option::attr(value)').extract()
        	item['img']=sel.css('a::attr(href)').extract_first()
        	yield item

        	next_page = response.xpath('//li/a[@rel="next"]/@href').extract_first()
        	if next_page is not None:
        		yield response.follow(next_page, self.parseproduct)