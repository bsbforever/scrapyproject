# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64
import linecache
import random 
# Start your middleware class
class ProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        file=open('/root/scrapy/proxy.txt','r')
        linecount=len(file.readlines())
        line=random.randint(1, linecount)
        proxy=linecache.getline('/root/scrapy/proxy.txt',line).strip().split()
        ip=proxy[0]
        port=proxy[1]
        # Set the location of the proxy
        #request.meta['proxy'] = "http://"+ip+":"+port
        request.meta['proxy'] = "http://61.190.68.178:80"
  
        # Use the following lines if your proxy requires authentication
        #proxy_user_pass = "USERNAME:PASSWORD"
        # setup basic authentication for the proxy
        #encoded_user_pass = base64.encodestring(proxy_user_pass)
        #request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
