# coding:utf8
from bs4 import BeautifulSoup
import urlparse
import re


class HtmlParser(object):
    """docstring for HtmlParser"""

    def _get_new_urls(self, pageurl, soup):
        if pageurl is None or soup is None:
            return
        new_urls = set()
        urls = soup.find_all('a', href=re.compile('/item/.*'))
        for url in urls:
            new_url = url['href']
            new_full_url = urlparse.urljoin(pageurl, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, pageurl, soup):
        if pageurl is None or soup is None:
            return
        new_data = {}
        html_title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        new_data['title'] = html_title.get_text()
        html_body =soup.find('div',class_='lemma-summary')
        new_data['body'] = html_body
        new_data['url'] = pageurl
        return new_data

    def parse(self, content, url):
        if url is None or content is None:
            return
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls,new_data