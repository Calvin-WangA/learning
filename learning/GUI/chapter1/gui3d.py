'''
Created on 2016年3月2日

@author: CasparWang
'''
import sys
from tkinter import *

class HelloCallable:
    def __init__(self):
        self.msg = 'Hello__call__world'
        
    def __call__(self):
        print(self.msg)
        sys.exit()
        
widget = Button(None,text='call',command=HelloCallable())
widget.pack()
widget.mainloop()