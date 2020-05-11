# -*- coding: utf-8 -*-
import scrapy


class NewbotSpider(scrapy.Spider):
    name = 'newbot'
    allowed_domains = ['https://www.phishtank.com/']
    start_urls = ['https://www.phishtank.com/phish_archive.php?page='+ str(id) for id in range(50,1000)]

    def parse(self, response):
        get_entered_date = response.css("table").css("tr").css("td:nth-child(2)").css("span::text").extract()
        phish_id = response.css("table").css("tr").css("td:nth-child(1)").css("a::text").extract()
        submitter = response.css("table").css("tr").css("td:nth-child(3)").css("a::text").extract()
        validity = response.css("table").css("tr").css("td:nth-child(4)").extract()
        online = response.css("table").css("tr").css("td:nth-child(5)").extract()
        
        for i in range(0, len(phish_id)-1):
            scraped_info = {
            'phish_id' : phish_id[i],
            'published_by' : submitter[i],
            'validity' : validity[i],
            'online' : online[i],
            'get_entered_date' : get_entered_date[i],              
            }
            
            yield scraped_info
