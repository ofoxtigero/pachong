#coding:utf8
import html_downloader
import html_parser


class SpiderMain(object):
    """docstring for SpiderMain"""
    def __init__(self, rooturl):
        self.rooturl = rooturl
    def craw(self):
        self.downloader = html_downloader.HtmlDownloader(self.rooturl)
        content = self.downloader.downloadPage()
        self.parser = html_parser.HtmlParser(content)
        self.parser.parse()
if __name__ == '__main__':
    url = 'http://baike.baidu.com/item/Python'
    spiderMain = SpiderMain(url);
    spiderMain.craw()

