#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
from datetime import datetime
import matplotlib
import matplotlib.dates as mdates
from matplotlib import pyplot as plt
from matplotlib.pyplot import plot,savefig

zhfont = matplotlib.font_manager.FontProperties(fname='./resource/msyh.ttf')

def add_weight(text):
    with open('./output/weight/our_weight.csv', 'a') as f:
        f.write(text+'\n')

def _build(msg):
    names,times,ws = [],[],[]
    for m in msg:
        t,name,w = m.replace(' ','').split(',')
        if t == 'timestamp':
            continue
        idx = None
        if name not in names:
            names.append(name)
            times.append([])
            ws.append([])
            idx = len(names)-1
        else:
            idx = names.index(name)
        #t = datetime.strptime(time.strftime("%Y-%m-%d %H:%M", time.localtime(float(t))), '%Y-%m-%d %H:%M').date()
        t = datetime.strptime(time.strftime("%Y-%m-%d %H:%M", time.localtime(float(t))), '%Y-%m-%d %H:%M')
        times[idx].append(t)
        ws[idx].append(float(w))
    print names
    print times
    print ws
    plt.figure(figsize=(30, 20))
    plt.xticks(fontproperties=zhfont, fontsize=25, rotation=20)
    plt.yticks(fontproperties=zhfont, fontsize=30)
    plt.title('体重大作战', fontproperties=zhfont, fontsize=40)
    plt.xlabel('参赛日期', fontproperties=zhfont, fontsize=30)
    plt.ylabel('体重(KG)', fontproperties=zhfont, fontsize=30)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    for i in range(len(times)):
        plt.plot(times[i], ws[i], linewidth=5, marker='o', markersize=15)
    plt.legend(labels=names, loc='best', fontsize=35) 
    savefig('./output/weight/weight_fight.png')
    return './output/weight/weight_fight.png'

def show_weight():
    msg = None
    with open('./output/weight/our_weight.csv', 'r') as f:
        msg = f.readlines()
    msg = [m for m in msg if m.split(',')[0]!='name']
    return _build(msg)
