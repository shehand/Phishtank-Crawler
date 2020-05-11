# -*- coding: utf-8 -*-
import scrapy
import csv
from collections import defaultdict

class PhishbotSpider(scrapy.Spider):
    columns = defaultdict(list)
    f = open(r'D:\Research\Pre_Evaluation\verified_online_updated.csv')
    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)
    name = 'phishbot'
    allowed_domains = ['https://www.phishtank.com/']
    start_urls = ['https://www.phishtank.com/phish_detail.php?phish_id='+id for id in columns['phish_id']]

    def parse(self, response):
        is_a_phish = response.css("h3").css("b::text").extract()
        published_by = response.css(".small").css("a::text").extract()
        verified_by = response.css("table").css("a::text").extract()
        is_phish_percentage = response.css(".isaphish::attr(width)").extract()
        is_not_phish_percentage = response.css(".isnotaphish::attr(width)").extract()
        phish_id = response.css("h2::text").extract()
        
        scraped_info = {
            'phish_id' : phish_id,
            'is_a_phish' : is_a_phish,
            'published_by' : published_by,
            'verified_by' : verified_by,
            'is_phish_percentage' : is_phish_percentage,
            'is_not_phish_percentage' : is_not_phish_percentage,               
        }
        yield scraped_info