#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os,sys,time
from datetime import datetime as dt

def todo():
    todo_str = 'Todo List:\n'
    with open('./output/todo/todo.csv', 'r') as f:
        for i,todo in enumerate(f.readlines()):
            todo = todo.strip('\n').strip().split('<::>')
            if todo[2] == 'delete':
                continue
            dt_ = dt.fromtimestamp(float(todo[1]))
            dt_str = str(dt_.month)+'-'+str(dt_.day)+' '+str(dt_.hour)+':'+str(dt_.minute)
            todo_str += '\t第'+str(i)+'条:'+dt_str+', '+todo[2]+', '+todo[3]+'\n'
    return todo_str

def addtodo(event):
    with open('./output/todo/todo.csv', 'a') as f:
        f.write(str(time.time())+'<::>'+str(time.time())+'<::>'+'idle'+'<::>'+event+'\n')

def update(idx, location, value):
    lines = None
    with open('./output/todo/todo.csv', 'r') as f:
        lines = f.readlines()
    with open('./output/todo/todo.csv', 'w') as f:
        for i,line in enumerate(lines):
            if i==idx:
                line = '<::>'.join([str(time.time()) if i==1 else (item if i != location else value) for i,item in enumerate(line.split('<::>'))])
            f.write(line)

def updatetodo(type_, idx):
    if type_ == 'start':
        starttodo(idx)
    elif type_ == 'pause':
        pausetodo(idx)
    elif type_ == 'finish':
        finishtodo(idx)
    elif type_ == 'delete':
        deltodo(idx)

def starttodo(idx):
    update(idx, 2, 'start')

def pausetodo(idx):
    update(idx, 2, 'pause')

def deltodo(idx):
    update(idx, 2, 'delete')

def finishtodo(idx):
    update(idx, 2, 'finish')

if __name__ == '__main__': 
    addtodo('基于微信....：增加todo功能')
    addtodo('今晚下班拿快递，快递柜')
    print todo()
    starttodo(0)
    starttodo(1)
    print todo()
    pausetodo(0)
    print todo()
    finishtodo(1)
    print todo()
    deltodo(0)
    print todo()
