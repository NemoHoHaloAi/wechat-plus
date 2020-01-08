#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PIL import Image
from PIL import ImageDraw

def logo(head_path, logo_path, tail_name):
    head = Image.open(head_path)
    add = Image.open(logo_path)
    add = add.resize((int(head.size[0]*2./5.), int(head.size[0]*2./5.*add.size[1]/add.size[0])),Image.ANTIALIAS)
    print add.size

    layer = Image.new('RGBA', head.size, (255,255,255,0))
    layer.paste(add, (head.size[0] - add.size[0], head.size[1]-add.size[1]))
    head_plus = Image.composite(layer, head, layer)
    head_plus.save(head_path[:head_path.rfind('.')]+tail_name+'.png')
    return head_path[:head_path.rfind('.')]+tail_name+'.png'

def flag(head_path):
    return logo(head_path, './resource/logo/flag.png', '_flag')

def dang_flag(head_path):
    return logo(head_path, './resource/logo/dangqi.png', '_dang')

if __name__ == '__main__': 
    print '1'
    # flag('./output/chat/head/head.jpg')

    # 国旗
    # flag = Image.open('./resource/logo/flag.png')
    # layer = Image.new('RGBA', (flag.size[0]+30, flag.size[1]+30), (255,255,255,0))
    # draw = ImageDraw.Draw(layer)
    # draw.ellipse((0, 0, flag.size[0]+30, flag.size[1]+30), 'white', 'white')
    # layer.paste(flag, (15, 15, flag.size[0]+15, flag.size[1]+15), flag)
    # layer.save('./resource/logo/flag_test.png')

    # 党旗
    # flag = Image.open('./resource/logo/dangqi.png')
    # layer = Image.new('RGB', (flag.size[0]+30, flag.size[1]+30), (255,255,255))
    # layer.paste(flag, (15, 15, flag.size[0]+15, flag.size[1]+15), flag)
    # layer.save('./resource/logo/dagnqi_test.png')
