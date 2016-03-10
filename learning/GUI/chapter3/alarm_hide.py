#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月10日

@author: Calvin Wang
'''
# customize to erase or show button on after() timer callbacks
from tkinter import *
import alarm

class Alarm(alarm.Alarm):
    def __init__(self,msec=1000):
        self.show = False
        alarm.Alarm.__init__(self,msec)
        
    def repeater(self):
        self.bell()
        if self.show:
            self.stopper.pack_forget()         # hide or erase button now
        else:
            self.stopper.pack()                # or reverse colors, flash...
        self.show = not self.show
        self.after(self.msec, self.repeater)
        
if __name__ == '__main__':
    Alarm(msec=5000).mainloop()