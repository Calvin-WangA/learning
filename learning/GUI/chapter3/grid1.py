#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月10日

@author: CasparWang
'''
from tkinter import *
colors = ['red','green','orange','yellow','white','blue']

r = 0
for c in colors:
    Label(text=c, relief=RIDGE, width=25).grid(row=r, column=0)
    Entry(bg=c, relief=SUNKEN, width=50).grid(row=r, column=1)
    r += 1
    
mainloop()