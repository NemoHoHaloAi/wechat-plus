#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# http://2.python-requests.org/zh_CN/latest/user/quickstart.html

'''
- sorry          # 抱歉，有钱就是可以为所欲为
- wangjingze     # 真香
- jinkela        # 金坷垃
- marmot         # 土拨鼠
- dagong         # 窃格瓦拉
- diandongche    # 窃格瓦拉偷电动车
'''

import os,sys,json
import requests as rq

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}#'Chrome/51.0.2704.63 Safari/537.36'}
host = 'https://sorry.xuty.tk'
url = host+'/api/{type}/make'

def sorry(texts, type_='sorry'):
    data_dict = {}
    for i, text in enumerate(texts):
        data_dict[str(i)] = text
    data = json.dumps(data_dict)
    rsp = rq.post(url.replace('{type}', type_), data, headers=headers, timeout=3)
    emoji_url = rsp.text
    os.system('http '+host+emoji_url+' > ./output/sorry/'+type_+'.gif') 
    return './output/sorry/'+type_+'.gif'

if __name__ == '__main__': 
    print sorry(['我肥涛今天就是全跪', '各种0/9/0，被人喷傻逼', '我也一定要打ADC', '嘿嘿嘿，其实辅助也不错'], 'wangjingze')
    print sorry(['肥涛', '你个菜逼'], 'marmot')
    print sorry(['Carry是不可能Carry的', '这辈子不可能Carry的', '打野上单中单辅助又不会', '就是ADC这种东西，勉强能操作', '到下路就像回家一样', '下路个个都是人才'], 'dagong')
    print sorry(['肥龙', '你打球厉害又怎么样', '长得像吴彦祖又怎么样', '我又不在乎', '我还是叫你肥龙', '我坚持吃沙拉减肥啊', '那又怎么样，这么久减了多少呢', '走吧辅良彪哥，撸串去'], 'sorry')
