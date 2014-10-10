#encoding=utf-8
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from banyungong.items import BanyungongItem

class BanyungongSpider(CrawlSpider):
    name = 'banyungong'
    allowed_domains = ['banyungong.net']
    start_urls = ['http://www.banyungong.net/']

    rules = (
        #Rule(SgmlLinkExtractor(allow=(r'/index\.html',)),follow=True),
        #Rule(SgmlLinkExtractor(allow=(r'/category/.*\.html',)),follow=True),
        #Rule(SgmlLinkExtractor(allow=(r'/search/.*\.html',)),follow=True),
        Rule(SgmlLinkExtractor(allow=('/magnetm/.*\.html', )),callback='parse_page', follow=False),
    )

    def parse_page(self, response):
        item = BanyungongItem()
        sel = Selector(response)
        type=sel.xpath('//a[@id="hlkType1"]/text()|//a[@id="hlkType2"]/text()').extract()
        #item['date']=sel.xpath('//span[@class="date"]/text()').extract()[0][`:-9]
        item['title'] = sel.xpath('//title/text()').extract()[0].split(',')[0]
        item['type']=sel.xpath('//a[@id="hlkType1"]/text()').extract()[0]
        #item['size']=sel.xpath('//span[@id="lblSize"]/text()').extract()[0]
        item['link'] = response.url
        return item
