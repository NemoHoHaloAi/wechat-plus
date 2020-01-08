#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# https://github.com/SavinaRoja/PyUserInput/blob/master/pykeyboard/windows.py

import time
from pykeyboard import *

kb = PyKeyboard()

def lock():
    kb.tap_key(kb.escape_key)
    time.sleep(2)
    kb.press_keys([kb.control_key,kb.alt_key,'l'])

def unlock():
    kb.tap_key(kb.escape_key)
    time.sleep(2)
    kb.press_key('D');kb.release_key('D') # 避免大写按键导致后续按键全部都是大写，因此不能把D和ongyuan写到一起
    kb.type_string('ongyuan8787')
    kb.tap_key(kb.enter_key)
    time.sleep(2)
    kb.tap_key(kb.enter_key)

def enter_delay():
    time.sleep(3)
    kb.tap_key(kb.enter_key)

def shot():
    pass
    ### thread.start_new_thread(enter_delay, ())
    ### os.system('gnome-screenshot')
    ### time.sleep(1)
    ### # so hard
    ### screenshot_name = "xxxx"
    ### os.system('mv '+screenshot_name+' ./output/screen/shot.png')

if __name__ == '__main__': 
    lock()
    time.sleep(5)
    unlock()
