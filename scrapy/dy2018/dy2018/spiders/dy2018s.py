#encoding=utf-8
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from dy2018.items import Dy2018Item
from scrapy.selector import Selector

class dy2018spider(CrawlSpider):
    name='dy2018'
    allowed_domains = ['dy2018.com']
    start_urls = ["http://www.dy2018.com"]
    rules = (
        #Rule(SgmlLinkExtractor(allow=(r'/\d+/$',)),follow=True),
        #Rule(SgmlLinkExtractor(allow=(r'/\d+/index_\d+.html',)),follow=True),
        #Rule(SgmlLinkExtractor(allow=(r'/i/\d+.html',)), callback="parse_item",follow=True),
        Rule(SgmlLinkExtractor(allow=(r'/i/\d+.html',)), callback="parse_item",follow=False),
        Rule(SgmlLinkExtractor(allow=(r'/html/\D+/\D+/\d+/\d+.html',)), callback="parse_item",follow=False),
    )


    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        item = Dy2018Item()
        sel = Selector(response)
        #item['title']=sel.xpath('//title/text()').extract()
        s=sel.xpath('//span/a[1]/text()').extract()
        j=sel.xpath('//a[re:test(@href, "/html/.*/.*/$")]/text()').extract()
        if s:
            item['type']=s
        else:
            item['type']=j
        item['title']=sel.xpath('//title/text()').extract()
        item['link']=response.url
        return item                                 
