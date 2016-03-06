#!/usr/local/bin/python
# coding: utf-8
'''
Created on 2016年3月6日

@author: Calvin Wang
'''
from learning.GUI.chapter2.imageButton import jpgdir
from tkinter import *
from PIL import ImageTk

win = Tk()
img = ImageTk.PhotoImage(file=jpgdir)
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2,2,image=img,anchor=NW)
win.mainloop()