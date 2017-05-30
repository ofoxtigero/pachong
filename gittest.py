# -*- coding: utf-8 -*-
import requests
import json

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def getuser():
    response = requests.get(build_uri('users/ofoxtigero'))
    print '>>>>Response headers'
    print response.headers
    print '>>>>Reponse body:'
    print better_print(response.text)
def getuseremail():
    response = requests.get(build_uri('user/emails'),auth=('ofoxtigero','eagle3325984'))
    print '>>>>Response headers'
    print response.headers
    print '>>>>Reponse body:'
    print better_print(response.text)

def getallusers():
    response = requests.get(build_uri('users'),params={'since':11})
    print '>>>>Response request headers'
    print response.request.headers
    print '>>>>Response request url'
    print response.url
    print '>>>>Reponse body:'
    print better_print(response.text)
if __name__ == '__main__':
    getallusers()