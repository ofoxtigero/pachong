#-*- coding:utf8 -*-
import urllib2
class HtmlDownloader(object):
    """docstring for HtmlDownloader"""
 
    def downloadPage(self,pageurl):
        if pageurl is None:
            return
        request = urllib2.Request(pageurl)
        request.add_header('User-Agent','Mozilla/5.0')
        response = urllib2.urlopen(request)

        if response.getcode() != 200:
            return
        return response.read() 
