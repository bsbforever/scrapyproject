#!/bin/sh 
cd /root/scrapy/cnbeta
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl cnbeta
