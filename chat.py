#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os,sys,time

from wordcloud import WordCloud as WC
import jieba
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.pyplot import savefig

zhfont = matplotlib.font_manager.FontProperties(fname='./resource/msyh.ttf')

jieba.load_userdict('./resource/customword.txt')
stopwords = set([line.strip().decode('utf-8') for line in open('./resource/stopword.txt', 'r').readlines()])

texts = []

DELIMITER = '<::>'

def build_wordcloud(msg):
    msg = ','.join([m.split(DELIMITER)[-1]for m in msg])
    words = list(jieba.cut(msg))
    for i in range(len(words)):
        if words[i] in stopwords:
            words[i] = ''
    wc = WC(font_path='./resource/msyh.ttf', #如果是中文必须要添加这个，否则乱码
        background_color='white',
        width=1000,
        height=800,).generate(' '.join(words))
    wc.to_file('./output/chat/message_cloud.png')
    return './output/chat/message_cloud.png'

def build_activity_user(msg):
    activity_dict = {}
    for m in msg:
        k,v = m.split(DELIMITER)[2:4] # 获取用户、文本
        activity_dict[k] = activity_dict.get(k, 0)+1
    activity_dict = dict((key, value) for key, value in activity_dict.items() if float(value) >= 10)
    plt.figure(figsize=(30, 20))
    plt.bar(range(len(activity_dict.keys())), activity_dict.values())
    fontsize_ = 15 if len(activity_dict.keys())>=30 else (30 if len(activity_dict.keys())>=20 else 35)
    plt.xticks(range(len(activity_dict.keys())), activity_dict.keys(), fontproperties=zhfont, rotation=90, fontsize=fontsize_)
    savefig('./output/chat/activity_user.png')
    return './output/chat/activity_user.png'

def build_activity_time(msg):
    hours = ['00点','01点','02点','03点','04点','05点','06点','07点','08点','09点','10点','11点',
                    '12点','13点','14点','15点','16点','17点','18点','19点','20点','21点','22点','23点']
    counts = [0]*len(hours)
    for m in msg:
        hour = time.localtime(float(m.split(DELIMITER)[1]))[3] # localtime得到一个struct_time元组，可以直接通过下标取值，3的位置是小时
        counts[hour] = counts[hour]+1
    plt.figure(figsize=(30, 20))
    plt.xticks(range(len(hours)), hours, fontproperties=zhfont, rotation=50, fontsize=30)
    plt.bar(range(len(counts)), counts)
    savefig('./output/chat/activity_time.png')
    return './output/chat/activity_time.png'

def build_longest_shortest(msg):
    longest, shortest = None, None
    activity_dict = {}
    for m in msg:
        k,v = m.split(DELIMITER)[2:4]
        activity_dict[k] = (activity_dict.get(k, (0,0))[0]+1,activity_dict.get(k, (0,0))[1]+len(v))
    activity_dict = dict((key, value[1]/value[0]) for key, value in activity_dict.items())
    shortest, longest = sorted(activity_dict.items(), key=lambda ad: ad[1])[::len(activity_dict.keys())-1]
    longest = '最长的人：'+str(longest[0])+'，平均长度：'+str(longest[1])
    shortest = '最短的人：'+str(shortest[0])+'，平均长度：'+str(shortest[1])
    return shortest+'\n'+longest

def chat(group_id, _len=1000):
    msg = None
    with open('./output/chat/text/wechat_message.csv', 'r') as f:
        msg = f.readlines()
    msg = msg[1:] # 去标头
    msg = [m for m in msg if m.startswith(group_id)]
    msg = msg[-_len:] # 只处理最近n行
    wc_path = build_wordcloud(msg)
    activity_user_path = build_activity_user(msg)
    activity_time_path = build_activity_time(msg)
    ls_str = build_longest_shortest(msg)
    return wc_path, activity_user_path, activity_time_path, ls_str

def add_message(group_id, msg):
    global texts
    if not os.path.exists('./output/chat/text/wechat_message.csv'):
        os.system('echo "groupid'+DELIMITER+'timestamp'+DELIMITER+'sender'+DELIMITER+'message" > ./output/chat/text/wechat_message.csv')
    texts.append(group_id+DELIMITER+str(time.time())+DELIMITER+(msg['ActualNickName'] if len(msg['ActualNickName'].strip())>0 else 'ANONYMOUS')+DELIMITER+(msg['Text'].replace('\n','').replace(' ','')))
    if len(texts) > 5:
        with open('./output/chat/text/wechat_message.csv', 'a') as f:
            for text in texts:
                f.write(text+'\n')
        texts = []

# git_sisr/something/knowledge/python/script/image_tool
def is_type_wrong(path):
    '''
    检查文件后缀是否与实际对应，例如实际是jpg，后缀是gif，导致打不开
    '''
    real_type = path[path.rfind('.')+1:]
    if path.lower().endswith('.gif') or path.lower().endswith('.jpg') or path.lower().endswith('.png'):
        header = []
        with open(path, 'rb') as f:
            while(len(header)<5):
                header.append(f.read(1))
        tmp = real_type
        if (header[0] == '\x47' and header[1] and '\x49' and header[2] == '\x46' and header[3] == '\x38'):
            tmp = 'gif'
        if (header[0] == '\xff' and header[1] == '\xd8'):
            tmp = 'jpg'
        if (header[0] == '\x89' and header[1] == '\x50' and header[2] == '\x4e' and header[3] == '\x47' and header[4] == '\x0D'):
            tmp = 'png'
        if real_type != tmp:
            return True,tmp
    return False,real_type

def add_else(group_id, from_user, msg):
    group_id = group_id.strip().strip('\t').strip('\n').replace('(','-').replace(')','-').replace('（','-').replace('）','-').replace(' ','-')
    name = from_user.strip().strip('\t').strip('\n').replace('(','-').replace(')','-').replace('（','-').replace('）','-').replace(' ','-')
    folder_path = './output/chat/'+msg['Type'].lower()+'/'+group_id
    if not os.path.exists(folder_path):
        os.system('mkdir '+folder_path)
    whole_name = folder_path+'/'+name+'-'+msg['FileName']
    msg['Text'](whole_name)
    if msg['Type'] == 'Picture':
        is_wrong,real_type = is_type_wrong(whole_name)
        if is_wrong:
            whole_name = whole_name.replace('\'', '\\\'')
            os.system('mv '+whole_name+' '+whole_name[:whole_name.rfind('.')]+'.'+real_type)
