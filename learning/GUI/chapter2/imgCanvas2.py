#!/usr/local/bin/python
#coding:  utf-8
'''
Created on 2016年3月6日

@author: Calvin Wang
'''
from learning.GUI.chapter2.imageButton import jpgdir
from sys import argv
from tkinter import *
from PIL.ImageTk import PhotoImage

filename = argv[1] if len(argv) > 1 else jpgdir     # filename on cmdline?

win = Tk()
img = PhotoImage(file=filename)
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(),height=img.height())   # set size to img's size 
can.create_image(2,2,image=img,anchor=NW)
win.mainloop()
