#encoding=utf-8
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from dy2018.items import Dy2018Item

class mydriversspider(CrawlSpider):
    name='mydrivers'
    allowed_domains = ['mydrivers.com']
    start_urls = ["http://www.mydrivers.com"]
    rules = (
        Rule(SgmlLinkExtractor(allow=(r'/1/318/318\d+.htm',)), callback="parse_page",follow=False),
    )


    def parse_page(self, response):
        item = Dy2018Item()
        sel = Selector(response)
        #item['title']=sel.xpath('//title/text()').extract() 
        item['title']=sel.xpath('//title/text()').extract()
        item['link']=response.url
        return item
