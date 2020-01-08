#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# http://2.python-requests.org/zh_CN/latest/user/quickstart.html

import os,sys,random
import requests as rq
from bs4 import BeautifulSoup as bs

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}#'Chrome/51.0.2704.63 Safari/537.36'}
url_search = 'https://home.meishichina.com/search/{key}/'

def search_meishi(key='家常菜'):
    os.system('rm -rf ./output/meishi')
    os.system('mkdir ./output/meishi')
    result = {}
    
    rsp = rq.get(url_search.replace('{key}', key), headers=headers, timeout=3)
    soup = bs(rsp.text, 'lxml')
    
    result['Title'] = soup.title.string
    
    result['List'] = soup.find('div', id='search_res_list')
    for i, child in enumerate(result['List'].children):
        if child.name == 'ul':
            result['List'] = child('li')
            break
    tmp_list = []
    for i, li in enumerate(result['List']):
        detail_dict = {}
        aaap = [element for element in li.find_all() if element.name in ['a', 'p']]
        if len(aaap) != 4:
            continue
        a1,a2,a3,p = aaap
        detail_dict['url'] = a1['href']
        detail_dict['img_url'] = a1('img')[0]['data-src'][2:a1('img')[0]['data-src'].lower().find('.jpg')+4]
        detail_dict['name'] = ''.join([content.encode('utf-8') for content in a2.contents]).replace('<em>','').replace('</em>','').replace(' ','')
        detail_dict['cooker'] = a3.string.replace(' ','')
        detail_dict['materials'] = ''.join([content.encode('utf-8') for content in p.contents]).replace('<em>','').replace('</em>','')
        tmp_list.append(detail_dict)

    result['List'] = tmp_list

    idx = random.randint(1, len(result['List']))
    item = result['List'][idx-1]
    item['title'] = result['Title']
    os.system('http '+item['img_url'] + ' > ./output/meishi/'+item['img_url'].replace('/','_'))
    item['img_path'] = './output/meishi/'+item['img_url'].replace('/','_')
    
    return item

if __name__ == '__main__': 
    search_meishi('腐竹')
