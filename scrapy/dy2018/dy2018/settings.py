# -*- coding: utf-8 -*-

# Scrapy settings for dy2018 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'dy2018'

SPIDER_MODULES = ['dy2018.spiders']
NEWSPIDER_MODULE = 'dy2018.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dy2018 (+http://www.yourdomain.com)'

'''DOWNLOADER_MIDDLEWARES = {
    'dy2018.middlewares.ProxyMiddleware': 1,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
}'''




ITEM_PIPELINES = {
    'dy2018.pipelines.dy2018MysqlStore':120,
}
LOG_LEVEL='DEBUG'
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True
#RETRY_ENABLED = False
#DOWNLOAD_TIMEOUT = 150'''
