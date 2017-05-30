#-*- coding=utf-8 -*-
import urllib2
import cookielib

url = 'http://www.baidu.com'

response1 = urllib2.urlopen(url)
print 'first method:'
print response1.getcode()
print len(response1.read())

request = urllib2.Request(url)
request.add_header('User-Agent','Mozilla/5.0')
response2 = urllib2.urlopen(request)
print 'second method:'
print response2.getcode()
print len(response2.read())



cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print 'third method'
print response3.getcode()
print response3.read()