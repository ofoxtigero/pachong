# -*- coding: utf-8 -*-
import requests

proxies = {'http':'socks5://127.0.0.1:1080','https':'socks5://127.0.0.1:8000'}

url = 'https://www.facebook.com'

response = requests.get(url,proxies=proxies,timeout=10)

print response.headers
print response.status_code