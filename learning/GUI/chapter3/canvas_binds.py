#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月10日

@author: CasparWang
'''
# bind events on both canvas and its Items
from tkinter import *

def onCanvasClick(event):
    print('Got canvas click', event.x, event.y, event.widget)
    
def onObjectClick(event):
    print('Got object click', event.x, event.y, event.widget, end=' ')
    print(event.widget.find_closest(event.x, event.y))   # find text object's ID
    
root = Tk()
canv = Canvas(root, width=100, height=100)
obj1 = canv.create_text(50,30, text='Click me one')
obj2 = canv.create_text(50,70, text='Click me two')

canv.bind('<Double-1>', onCanvasClick)
canv.tag_bind(obj1, '<Double-1>', onObjectClick)
canv.tag_bind(obj2, '<Double-1>', onObjectClick)
canv.pack()

root.mainloop()