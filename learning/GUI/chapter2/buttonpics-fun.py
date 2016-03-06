#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月6日

@author: Calvin Wang
'''
from tkinter import *
from glob import glob
from PIL.ImageTk import PhotoImage
import demoCheck
import random

jpgpath = 'F:\Python\images\*.jpg'

def draw():
    name, photo = random.choice(images)
    lbl.config(text=name)
    pix.config(image=photo)
    
root = Tk()
lbl = Label(root, text="none",bg='blue', fg='red')
pix = Button(root,text="Press Me",command=draw,bg='white')
lbl.pack(fill=BOTH)
pix.pack(pady=10)
demoCheck.Demo(root,relief=SUNKEN,bd=2).pack(fill=BOTH)

files = glob(jpgpath)
images = [(x,PhotoImage(file=x)) for x in files ]
print(files)
root.mainloop()

