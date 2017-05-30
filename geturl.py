# -*- coding: utf-8 -*-
import urllib2
import urllib

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'
def use_simple_lib2():
    response = urllib2.urlopen(URL_IP)
    print '>>>> Response header'
    print response.info()
    print '>>>> Response body:'
    print ''.join([line for line in response.readlines()])

def use_simple_get():
    params = urllib.urlencode({'param1':'hello','param2':'world'})
    print 'request params'
    print params
    print '%s' % params
    response = urllib2.urlopen('?'.join([URL_GET,'%s']) % params)
    print '>>>> Response header'
    print response.info()
    print '>>>> Response body:'
    print ''.join([line for line in response.readlines()])

if __name__ == '__main__':
    #use_simple_lib2()
    use_simple_get()