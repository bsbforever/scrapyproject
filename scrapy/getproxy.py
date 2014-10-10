#!/usr/bin/python
#coding=gbk
#coding=utf-8
import os
from lxml import *
import lxml.html
import urllib2
import lxml.html as H
proxy=[]
k=1
n=1
m=''
url="http://www.proxy360.cn/default.aspx"
c=urllib2.urlopen(url)
f=c.read()
doc = H.document_fromstring(f)
result=doc.xpath('//div[@class="proxylistitem"]/div/span[@class="tbBottomLine"][position()<3]/text()')
for i in result:
    if n<=20:
        j=i.strip()
        proxy.append(j)
        n=n+1
for i in proxy:
    if k%2==1:
        m=m+i+'\t'
        k=k+1
    else:
        m=m+i+'\n'
        k=k+1
print m
fp = open(r"/root/scrapy/proxy.txt",'w')
fp.write(m)
fp.close()
