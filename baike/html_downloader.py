#-*- coding:utf8 -*-
import urllib2
class HtmlDownloader(object):
    """docstring for HtmlDownloader"""
    def __init__(self,pageurl):
        self.pageurl = pageurl
    def downloadPage(self):
        if self.pageurl is None:
            return None
        request = urllib2.Request(self.pageurl)
        request.add_header('User-Agent','Mozilla/5.0')
        response = urllib2.urlopen(request)

        if response.getcode() != 200:
            return None
        return response.read() 
