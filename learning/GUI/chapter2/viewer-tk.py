#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月6日

@author: Calvin Wang
'''
from tkinter import *
from PIL.ImageTk import PhotoImage
import sys,os

imgdir = 'F:\Python\images'
imgfile = '331018.jpg'
if len(sys.argv) > 1:
    imgdir = sys.argv[1] 
imgpath = os.path.join(imgdir,imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath)
Label(win,image=imgobj).pack()
print(imgobj.width(),imgobj.height())
win.mainloop()