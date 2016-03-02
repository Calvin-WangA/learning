'''
Created on 2016年3月2日

@author: CasparWang
'''
from tkinter import *

def greeting():
    print('Hello stdouot world')
    
win = Frame()
win.pack()

Label(win,text='Hello container world').pack(side=TOP)
Button(win,text='Hello',command=greeting).pack(side=LEFT)
Button(win,text='Quit',command=quit).pack(side=RIGHT)

win.mainloop()