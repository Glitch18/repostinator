# -*- coding: utf-8 -*-
import scrapy


class RedditcrawlerSpider(scrapy.Spider):
    name = 'redditCrawler'
    allowed_domains = ['reddit.com']
    start_urls = [
                    'http://www.reddit.com/r/meirl',
                    'http://www.reddit.com/r/memes',
                    'http://www.reddit.com/r/me_irl',
                    'http://www.reddit.com/r/absolutelynotme_irl',]

    def getImageUrl(self,response):
        l = response.xpath('//a/@href').getall()
        l = [x for x in l if 'i.redd.it' in x or 'external-preview.redd.it' in x]
        if len(l)==0:
            return
        author = response.xpath("//a[@class='_2tbHP6ZydRpjI44J3syuqC fmmy6j-1 eWFTds']/text()").get()
        with open('img_urls.txt', 'a+') as f:
            f.write("{}^^{}\n".format(l[0],author))


    def parse(self, response):
        l = response.xpath('//a/@href').getall()
        l = [x for x in l if 'reddit' in x and 'comments' in x]

        for i in l:
            yield scrapy.Request(url=i,callback=self.getImageUrl)

        with open('post_urls.txt', 'w') as f:
            for item in l:
                f.write("%s\n" % item)
