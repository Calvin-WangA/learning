#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月10日

@author: Calvin Wang
'''
# flash and beep every second using after() callback loop
from tkinter import *

class Alarm(Frame):
    def __init__(self,msec=1000):
        Frame.__init__(self)
        self.msec = msec
        self.pack()
        stopper = Button(self, text='Stop the beeps!', command=self.quit)
        stopper.pack()
        stopper.config(bg='navy', fg='white', bd=8)
        self.stopper = stopper
        self.repeater()
        
    def repeater(self):                       # on every N millises
        self.bell()                           # beep now
        self.stopper.flash()                  # flash botton now
        self.after(self.msec, self.repeater)  # reschedule handler
        
if __name__ == '__main__':
    Alarm(msec=5000).mainloop()
