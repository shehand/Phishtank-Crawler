# -*- coding: utf-8 -*-
import scrapy
import csv
from collections import defaultdict

class NewbotSpider(scrapy.Spider):
    columns = defaultdict(list)
    f = open(r'D:\Research\Pre_Evaluation\my_df.csv')
    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)
    name = 'newbot'
    allowed_domains = ['https://www.phishtank.com/']
    start_urls = ['https://www.phishtank.com/user.php?username='+ name for name in columns['user']]

    def parse(self, response):
        user = response.css(".user").css(".value::text").extract()
        user_name = response.css("h2::text").extract()
        website = response.css(".user").css(".value").css("a::text").extract()
        count = response.css("h3").css("b::text").extract()
        real_name = ""
        member_since = ""
        last_verifier = ""
        submissions = count[0]
        verifications = count[1]
        dates = response.css(".data").css("tr").css("td:nth-child(2)").css(".small::text").extract()
        
        if len(user) == 2:
            real_name = user[0]
            member_since = user[1]
        else:
            member_since = user[0]
        
        if len(dates) > 5:
            last_verifier = dates[5]
            
        scraped_info = {
            'user_name' : user_name,
            'member_since-date': member_since,
            'real_name' : real_name,
            'website' : website,
            'submission_count' : submissions,
            'verification_count' : verifications,
            'last_verified_date' : last_verifier,               
        }
        yield scraped_info