#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月10日

@author: Calvin Wang
'''
# same ,but hide or show entire window on after() timer callbacks
from tkinter import *
import alarm

class Alarm(alarm.Alarm):
    def repeater(self):
        self.bell()
        if self.master.state() == 'normal':    # is window displayed?
            self.master.withdraw()             # hide entire window, no icon
        else:
            self.master.deiconify()            # else redraw entire window
            self.master.lift()                 # and raise above others
        self.after(self.msec, self.repeater)
        
if __name__ == '__main__':
    Alarm().mainloop()