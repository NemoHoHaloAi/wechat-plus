#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# https://github.com/MZCretin/RollToolsApi

import os,sys,json,random
import requests as rq 

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}#'Chrome/51.0.2704.63 Safari/537.36'}
url_search = 'https://www.mxnzp.com/api/image/girl/list/random'

def search_girl():
    rsp = rq.get(url_search, headers=headers, timeout=3)
    rsp_dict = rsp.json()
    if rsp_dict['code'] == 1:
        girl_url = rsp_dict['data'][random.randint(1,len(rsp_dict['data']))-1]['imageUrl']
        os.system('http '+girl_url+' > ./output/girl/girl.png')
        return './output/girl/girl.png'

if __name__ == '__main__': 
    print search_girl()
