#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os,sys,time,thread
reload(sys)
sys.setdefaultencoding('utf8')

import itchat

from chat import chat,add_message,add_else
from meishi import search_meishi
from weather import search_city_weather
from joke import search_joke
from girl import search_girl
from screen import lock,unlock,shot
from weight import add_weight,show_weight
from emoji import search_emoji
from sorry import sorry
from todo import todo,addtodo,updatetodo
from baidu import translate
from tts import offline_tts, online_tts, online_tts_new
from logo_plus import flag, dang_flag

texts = []
group_id = None
from_user = None

def dolist():
    functionlist = '功能列表：\n'
    functionlist += '\tHoLoong：获取当前群聊的消息分析内容；\n'
    functionlist += '\t#体重#：获取体重跟踪数据，通过weight,姓名,体重（公斤）记录；\n'
    functionlist += '\t远程控制：\n'
    functionlist += '\t\t#锁屏#：远程锁屏；\n'
    functionlist += '\t\t#解锁#：远程解锁；\n'
    functionlist += '\t\t#截屏#：获取屏幕截图（临时停用）；\n'
    functionlist += '\t#美食#烤鸭：随机获取相关美食；\n'
    functionlist += '\t#天气#北京：获取对应城市当天天气；\n'
    functionlist += '\t#笑话#：随机获取笑话一则；\n'
    functionlist += '\t#福利#：随机获取妹子图一张；\n'
    functionlist += '\t#表情包#傻逼：随机获取相关表情包；\n'
    functionlist += '\t表情包制作：\n'
    functionlist += '\t\t#抱歉#xxx：构造sorry图一张；\n'
    functionlist += '\t\t#真香#xxx：构造真香图一张；\n'
    functionlist += '\t\t#土拨鼠#xxx：构造土拨鼠图一张；\n'
    functionlist += '\t\t#窃格瓦拉#xxx：构造窃格瓦拉打工图一张；\n'
    functionlist += '\tTODO：\n'
    functionlist += '\t\t#todo#：展示todo列表；\n'
    functionlist += '\t\t#addtodo#xxx：增加一条todo；\n'
    functionlist += '\t\t#starttodo#idx：开始一条todo；\n'
    functionlist += '\t\t#pausetodo#idx：暂停一条todo；\n'
    functionlist += '\t\t#finishtodo#idx：结束一条todo；\n'
    functionlist += '\t\t#deltodo#idx：删除一条todo；\n'
    functionlist += '\t翻译：\n'
    functionlist += '\t\t#英语#你好：翻译成英语；\n'
    functionlist += '\t\t#中文#你好：翻译成中文；\n'
    functionlist += '\t\t#日语#你好：翻译成日语；\n'
    functionlist += '\t\t#韩语#你好：翻译成韩语；\n'
    functionlist += '\t\t#粤语#你好：翻译成粤语；\n'
    itchat.send(functionlist, 'filehelper')

def dodemo(text):
    demo_str = ''
    if text == '美食':
        demo_str = '#美食#凉菜'
    elif text == '天气':
        demo_str = '#天气#天津'
    elif text == '表情包':
        demo_str = '#表情包#傻了吧'
    elif text == '抱歉':
        demo_str = '#抱歉#肥龙。你打球厉害又怎么样。长得像吴彦祖又怎么样。我又不在乎。我还是叫你肥龙。我坚持吃沙拉减肥啊。那又怎么样，这么久减了多少呢。走吧辅良彪哥，撸串去'
    elif text == '真香':
        demo_str = '#真香#我今天就是饿死。从这死出去。我也不吃这碗饭。真香'
    elif text == '土拨鼠':
        demo_str = '#土拨鼠#谁阿。打游戏呢'
    elif text == '窃格瓦拉':
        demo_str = '#窃格瓦拉#Carry是不可能Carry的。这辈子不可能Carry的。打野上单中单辅助又不会。就是ADC这种东西，勉强能操作。到下路就像回家一样。下路个个都是人才'
    else:
        pass
    itchat.send(demo_str, group_id)

def dochattext(msg):
    add_message(group_id, msg)

def dochatelse(from_user, msg):
    add_else(group_id, from_user, msg)

def dochat():
    wc_path, user_path, time_path, ls_str = chat(group_id)
    if wc_path != None:
        itchat.send_image(wc_path, group_id)
    if user_path != None:
        itchat.send_image(user_path, group_id)
    if time_path != None:
        itchat.send_image(time_path, group_id)
    if ls_str != None:
        itchat.send(ls_str, group_id)

def doaddweight(text):
    row = str(time.time())+','+str(text.split(',')[1])+','+str(text.split(',')[2])
    if row != None:
        add_weight(row)

def doweight():
    image_path = show_weight()
    if image_path != None:
        itchat.send_image(image_path, group_id)

def dolock():
    lock()
    itchat.send('Locking....', group_id)

def dounlock():
    unlock()
    itchat.send('Unlocking....', group_id)

def doshot():
    shot_path = shot()
    if shot_path != None:
        itchat.send_image(shot_path, group_id)

def domeishi(key='家常菜'):
    item = search_meishi(key)
    if item != None:
        result_str = item['title']+'：\n'
        result_str += '\t===================\n'
        result_str += '\t菜名：'+item['name']+'\n'
        result_str += '\t厨师：'+item['cooker']+'\n'
        result_str += '\t'+item['materials']+'\n'
        result_str += '\t详情链接：'+item['url']+'\n'
        itchat.send(result_str, group_id)
        itchat.send_image(item['img_path'], group_id)

def doweather(city='北京'):
    result = search_city_weather(city)
    if result != None:
        result_str = '位置：'+result[0]+'\n'
        result_str += '温度：'+result[1]+'\n'
        result_str += '天气：'+result[2]+'\n'
        result_str += '湿度：'+result[3]
        itchat.send(result_str, group_id)

def dojoke():
    joke = search_joke()
    if joke != None:
        itchat.send(joke, group_id)

def dogirl():
    girl_path = search_girl()
    if girl_path != None:
        itchat.send_image(girl_path, group_id)

def doemoji(key):
    emoji_path = search_emoji(key)
    if emoji_path != None:
        itchat.send_image(emoji_path, group_id)

def dosorry(text, type_):
    sorry_path = sorry(text.strip('\n').strip().split('。'), type_)
    if sorry_path != None:
        itchat.send_image(sorry_path, group_id)

def dotodo(type_=None, event=None, idx=None):
    if event:
        addtodo(event)
    if type_ and (not idx is None):
        updatetodo(type_, idx)
    itchat.send(todo(), group_id)

def dotranslate(text, to_):
    result_str = translate(text, to_=to_)
    itchat.send(result_str, group_id)

def dologoplus(msg, type_='flag'):
    itchat.get_head_img(userName=msg['ActualUserName'], chatroomUserName=group_id, picDir='./output/chat/head/'+msg['ActualUserName']+'.jpg')
    logo_path = None
    if type_ == 'flag':
        logo_path = flag('./output/chat/head/'+msg['ActualUserName']+'.jpg')
    elif type_ == 'dang':
        logo_path = dang_flag('./output/chat/head/'+msg['ActualUserName']+'.jpg')

    itchat.send_image(logo_path, group_id)


#dolist()
#dochat()
#doweight()
#dolock()
#dounlock()
#doshot()
#domeishi('豆腐')
#doweather('上海')
#dojoke()
#dogirl()
#doemoji('拉屎')
#exit()
@itchat.msg_register([itchat.content.ATTACHMENT, itchat.content.PICTURE, itchat.content.VIDEO, itchat.content.RECORDING], isFriendChat=True, isGroupChat=True)
def else_recv(msg):
    global group_id, from_user

    from_user = None
    if 'ActualUserName' in msg.keys() and msg['ActualUserName'] == msg['FromUserName']:
        group_id = msg['ToUserName']
        from_user = msg['ActualNickName']
    else:
        group_id = msg['FromUserName']
        from_user = msg['FromUserName']
    print '群聊：'+str(group_id)
    print '用户：'+str(from_user)
    print '类型：'+str(msg['Type'])+'\n'
    dochatelse(from_user, msg)

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    global group_id

    from_user = None
    if msg['ActualUserName'] == msg['FromUserName']:
        group_id = msg['ToUserName']
    else:
        group_id = msg['FromUserName']
    print '群聊：'+str(group_id)
    print '用户：'+str(msg['ActualNickName'])
    print '文本：'+str(msg['Text'])+'\n'
    dochattext(msg)

    if msg['Text'].find('#功能#') != -1:
        dolist()
    if msg['Text'].find('#例子#') != -1:
        dodemo(msg['Text'].replace('#例子#', ''))
    elif msg['Text'].find('HoLoong') != -1:
        dochat()
    elif msg['Text'].find('#锁屏#') != -1:
        dolock()
    elif msg['Text'].find('#解锁#') != -1:
        dounlock()
    elif msg['Text'].find('#截屏#') != -1:
        pass
        # doshot()
    elif msg['Text'].find('#美食#') != -1:
        domeishi(msg['Text'].replace('#美食#', ''))
    elif msg['Text'].find('#天气#') != -1:
        doweather(msg['Text'].replace('#天气#', ''))
    elif msg['Text'].find('#笑话#') != -1:
        dojoke()
    elif msg['Text'].find('#福利#') != -1:
        dogirl()
    elif msg['Text'].find('#表情包#') != -1:
        doemoji(msg['Text'].replace('#表情包#', ''))
    elif msg['Text'].find('#体重#') != -1:
        doweight()
    elif msg['Text'].startswith('weight,'):
        doaddweight(msg['Text'])
    elif msg['Text'].find('#抱歉#') != -1:
        dosorry(msg['Text'].replace('#抱歉#', ''), 'sorry')
    elif msg['Text'].find('#真香#') != -1:
        dosorry(msg['Text'].replace('#真香#', ''), 'wangjingze')
    elif msg['Text'].find('#土拨鼠#') != -1:
        dosorry(msg['Text'].replace('#土拨鼠#', ''), 'marmot')
    elif msg['Text'].find('#窃格瓦拉#') != -1:
        dosorry(msg['Text'].replace('#窃格瓦拉#', ''), 'dagong')
    elif msg['Text'].find('#todo#') != -1:
        pass
        # dotodo()
    elif msg['Text'].find('#addtodo#') != -1:
        pass
        # dotodo(type_='add', event=msg['Text'].replace('#addtodo#', ''))
    elif msg['Text'].find('#starttodo#') != -1:
        pass
        # dotodo(type_='start', idx=int(msg['Text'].replace('#starttodo#', '')))
    elif msg['Text'].find('#pausetodo#') != -1:
        pass
        # dotodo(type_='pause', idx=int(msg['Text'].replace('#pausetodo#', '')))
    elif msg['Text'].find('#finishtodo#') != -1:
        pass
        # dotodo(type_='finish', idx=int(msg['Text'].replace('#finishtodo#', '')))
    elif msg['Text'].find('#deltodo#') != -1:
        pass
        # dotodo(type_='delete', idx=int(msg['Text'].replace('#deltodo#', '')))
    elif msg['Text'].find('#英语#') != -1:
        dotranslate(msg['Text'].replace('#英语#', ''), 'en')
    elif msg['Text'].find('#中文#') != -1:
        dotranslate(msg['Text'].replace('#中文#', ''), 'zh')
    elif msg['Text'].find('#日语#') != -1:
        dotranslate(msg['Text'].replace('#日语#', ''), 'jp')
    elif msg['Text'].find('#韩语#') != -1:
        dotranslate(msg['Text'].replace('#韩语#', ''), 'kor')
    elif msg['Text'].find('#粤语#') != -1:
        dotranslate(msg['Text'].replace('#粤语#', ''), 'yue')
    elif msg['Text'].find('#国旗#') != -1:
        dologoplus(msg)
    elif msg['Text'].find('#党旗#') != -1:
        dologoplus(msg, type_='dang')
    else:
        pass

itchat.auto_login(hotReload=True)
itchat.run()
