#coding:utf8
from html_downloader import HtmlDownloader
from  html_parser import HtmlParser
from  url_manage import UrlManage
from html_outputer import HtmlOutputer

class SpiderMain(object):
    """docstring for SpiderMain"""
    def __init__(self):
        self.urlManage = UrlManage()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.outputer = HtmlOutputer()
    def craw(self,url):
        self.urlManage.add_new_url(url)
        
        count = 1
        while self.urlManage.has_new_url():
            url = self.urlManage.get_new_url()
            print '%dth page,address:%s' % (count,url)
            html_content = self.downloader.downloadPage(url)
            new_urls,new_data = self.parser.parse(html_content,url)
            self.urlManage.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)

            if count == 10:
                break

            count = count + 1 
        self.outputer.output_html()

if __name__ == '__main__':
    url = 'http://baike.baidu.com/item/Java'
    spiderMain = SpiderMain();
    spiderMain.craw(url)

