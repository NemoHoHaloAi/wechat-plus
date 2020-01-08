#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# https://github.com/MZCretin/RollToolsApi

import os,sys,json
import requests as rq 

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}#'Chrome/51.0.2704.63 Safari/537.36'}
url_search = 'https://www.mxnzp.com/api/weather/current/{city}'
key = '{city}'

def search_city_weather(city='深圳'):
    rsp = rq.get(url_search.replace(key, city), headers=headers, timeout=3)
    rsp_dict = rsp.json()
    result = []
    if rsp_dict['code'] == 1:
        print '天气获取成功'
        print 'Address:'+rsp_dict['data']['address']
        result.append(rsp_dict['data']['address'])
        print 'Temp:'+rsp_dict['data']['temp']
        result.append(rsp_dict['data']['temp'])
        print 'Weather:'+rsp_dict['data']['weather']
        result.append(rsp_dict['data']['weather'])
        print 'Humidity:'+rsp_dict['data']['humidity']
        result.append(rsp_dict['data']['humidity'])
    else:
        print '天气获取失败'
        print rsp_dict['msg']
    return result

if __name__ == '__main__': 
    print search_city_weather('北京')
