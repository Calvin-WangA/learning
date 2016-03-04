'''
Created on 2016年3月1日

@author: CasparWang
'''
import sys
from tkinter import *

def quit():
    print('Hello i must be going...')
    sys.exit()
    
widget = Button(None,text='exit',command=quit)
widget.pack()
widget.mainloop()
