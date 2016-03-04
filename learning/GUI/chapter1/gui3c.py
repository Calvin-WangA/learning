'''
Created on 2016年3月2日

@author: CasparWang
'''
import sys
from tkinter import *

class HelloClass:
    def __init__(self):
        widget = Button(None,text='Hello event world',command=sys.exit)
        widget.pack()
    def quit(self):
        print('Hello class method world')
        sys.exit()
        
if __name__ == '__main__':
    HelloClass()
    mainloop()