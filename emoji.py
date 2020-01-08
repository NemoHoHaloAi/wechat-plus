#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os,sys,json,random
import requests as rq 
from bs4 import BeautifulSoup as bs

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}#'Chrome/51.0.2704.63 Safari/537.36'}
url_search = 'https://www.fabiaoqing.com/search/search/keyword/{key}'

def search_emoji(key='熊猫头'):
    rsp = rq.get(url_search.replace('{key}',key), headers=headers, timeout=3)
    soup = bs(rsp.text, 'lxml')
    emojis = soup.find_all('div', class_='searchbqppdiv tagbqppdiv')
    emoji_url = emojis[random.randint(1,len(emojis))-1].a.img['data-original']
    os.system('http '+emoji_url+' > ./output/emoji/emoji'+emoji_url[emoji_url.rfind('.'):])
    return './output/emoji/emoji'+emoji_url[emoji_url.rfind('.'):]

if __name__ == '__main__': 
    print search_emoji('拉屎')
