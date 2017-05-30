#coding:utf8
from bs4 import BeautifulSoup
import re
class HtmlParser(object):
    """docstring for HtmlParser"""
    def __init__(self, content):
        self.content = content

    def parse(self):
        soup = BeautifulSoup(self.content,'html.parser',from_encoding='utf-8')
        urls = soup.find_all('a',href=re.compile('/item/.*'))
        for url in urls:
            print url.name,url['href']