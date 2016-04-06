#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月21日

@author: CasparWang
'''
from tkinter.messagebox import askyesno
from tkinter.constants import *

def copyText(text):
        print("selected text is "+text.get(SEL_FIRST,SEL_LAST))
