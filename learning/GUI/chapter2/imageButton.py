#!/usr/local/bin/python
# coding: utf-8
'''
Created on 2016年3月4日
@author: Calvin Wang
'''
jpgdir = 'MIMI.jpg'
from tkinter import *
from PIL import ImageTk

root = Tk()
photoimg = ImageTk.PhotoImage(file=jpgdir)
Button(root,image=photoimg).pack()
root.mainloop()