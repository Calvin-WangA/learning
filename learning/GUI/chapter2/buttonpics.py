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

class ButtonPicsDemo(Frame):
    def __init__(self,parent=None,**options):
        Frame.__init__(self,parent,**options)
        self.pack()
        self.lbl = Label(self,text='none',bg='blue',fg='red')
        self.pix = Button(self,text='Press Me',command=self.draw,bg='white')
        self.lbl.pack(fill=BOTH)
        self.pix.pack(pady=10)
        demoCheck.Demo(self,relief=SUNKEN,bd=2).pack(fill=BOTH)
        files = glob(jpgpath)
        self.images = [(x,PhotoImage(file=x)) for x in files]
        print(files)
        
    def draw(self):
        name,photo = random.choice(self.images)
        self.lbl.config(text=name)
        self.pix.config(image=photo)
        
if __name__ == '__main__':
    ButtonPicsDemo().mainloop()