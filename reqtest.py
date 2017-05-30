# -*- coding: utf-8 -*-
import requests

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'

def use_simple_requests():
    response = requests.get(URL_IP)
    print '>>>> Response header'
    print response.headers
    print '>>>> Response body:'
    print response.text


def use_params_requests():
    params = {'param1':'hello','param2':'world'}
    print 'request params'
    print params
    response = requests.get(URL_GET,params=params)
    print '>>>> Response header'
    print response.headers
    print '>>>> Response body:'
    print response.text
    print '>>>> Response json'
    print response.json()

if __name__ == '__main__':
    #use_simple_lib2()
    # use_simple_requests()
    use_params_requests()