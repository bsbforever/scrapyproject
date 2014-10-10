#encoding=utf-8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
#from scrapy.contrib.pipeline.images import ImagesPipeline
from cnbeta.items import CnbetaItem
import time
import MySQLdb
import MySQLdb.cursors

class CnbetaPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', db='mysql',
                user='root', passwd='123456', cursorclass=MySQLdb.cursors.DictCursor,
                charset='utf8', use_unicode=True)
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
 
        return item

    def _conditional_insert(self, tx, item):
        tx.execute("select * from navigation_cnbeta  where title= %s",(item['title'][0],))
        result=tx.fetchone()
        log.msg(result,level=log.DEBUG)
        print result
        if result:
            log.msg("Item already stored in db:%s" % item,level=log.DEBUG)
        else:
        # create record if doesn't exist. 
        # all this block run on it's own thread
            if item.get('title'):
                tx.execute(\
                    "insert into navigation_cnbeta (date,title,link) values (%s,%s, %s)",
                    (item['date'],
                    item['title'][0].encode('utf8'),
                    item['link'])
                    )
                #tx.close() 
    def handle_error(self, e):
        log.err(e)
