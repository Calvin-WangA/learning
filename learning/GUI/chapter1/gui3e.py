'''
Created on 2016年3月2日

@author: CasparWang
'''
import sys
from tkinter import *

def hello(event):
    print('Press twice to exit')
    
def quit(event):
    print('Hello, i must be going')
    sys.exit()
    
widget = Button(None,text='Hello event world')
widget.pack()
widget.bind('<Button-1>',hello)
widget.bind('<Double-1>',quit)
widget.mainloop()
