#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os,sys,random,time,json,hashlib
import requests as rq

# http://api.fanyi.baidu.com/api/trans/product/desktop?req=developer
'''
'auto':'自动检测','zh':'中文','en':'英语','yue':'粤语','wyw':'文言文','jp':'日语','kor':'韩语','fra':'法语','spa':'西班牙语','th':'泰语','ara':'阿拉伯语','ru':'俄语','pt':'葡萄牙语','de':'德语','it':'意大利语','el':'希腊语','nl':'荷兰语','pl':'波兰语','bul':'保加利亚语','est':'爱沙尼亚语','dan':'丹麦语','fin':'芬兰语','cs':'捷克语','rom':'罗马尼亚语','slo':'斯洛文尼亚语','swe':'瑞典语','hu':'匈牙利语','cht':'繁体中文','vie':'越南语'
'''

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}#'Chrome/51.0.2704.63 Safari/537.36'}
host = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
id_ = 'Your id'
secret = 'Your secret'

support_language_list = {'中文':'ch', '英语':'en', '日语':'jp', '韩语':'kor', '粤语':'yue'}

def translate(text, from_='auto', to_='en'):
    salt = str(random.randint(0,99999999))
    #sign = hashlib.md5(id_+text.encode(encoding='UTF-8')+salt+secret).hexdigest()
    sign = hashlib.md5(id_+text+salt+secret).hexdigest()
    prs = {'q':text, 'from':from_, 'to':to_, 'appid':id_, 'salt':salt, 'sign':sign}
    rsp = rq.post(host, params=prs, headers=headers, timeout=3)
    result_dict = rsp.json()
    return result_dict['trans_result'][0]['dst']

if __name__ == '__main__': 
    print translate('我爱你中国，亲爱的母亲，我为你骄傲', to_='en')
    time.sleep(1)
    print translate('come to fight me', to_='zh')
