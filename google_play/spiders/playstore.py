# -*- coding: utf-8 -*-
import scrapy
def get_urls():
        s_urls = []
        with open('/Users/sunilmanandhar/Documents/SecurityResearch/privacy_iot/scraping/latest.csv','r') as fromFile:
            next(fromFile)
            for line in fromFile:
                s_urls.append('https://play.google.com/store/apps/details?id=' + line.split(',')[5].replace('"',''))
        return s_urls

class PlaystoreSpider(scrapy.Spider):
    name = 'playstore'
    allowed_domains = ['play.google.com']
    # start_urls = ['http://play.google.com/']

    #list of allowed domains
    # allowed_domains = ['https://play.google.com/store/apps/details?id=]

    #starting url for scraping
    start_urls = get_urls()

    #setting the location of the output csv file
    custom_settings = {
        'FEED_URI' : './playstore_links.csv'
    }

    

    def parse(self, response):
        # policy_document = str(response.xpath('//a[contains(text(), "Privacy Policy")]').extract())
        url_crawl = response.request.url
        policy_document = str(response.xpath('//a[contains(text(), "Privacy Policy")]/@href').extract()[0])   
        for d in response.css('div'): 
            if('jsname' in d.attrib.keys()): 
                if(d.attrib['jsname'] == 'sngebd'): 
                    #description = str(d.extract())
                    description = ' '.join(d.css('div *::text').getall())
                    # description = d.css('div *::text').getall()

        # for item in zip(policy_document,description):
        scraped_info = {
            'crawl_url' : url_crawl,
            'policy_document' : policy_document,
            'description' : description,

        }

        yield scraped_info