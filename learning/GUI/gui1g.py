'''
Created on 2016年3月1日

@author: CasparWang
'''
from tkinter import *

root = Tk()
widget = Label(root)
widget.config(text='Hello GUI World!')
widget.pack(side=TOP,expand=YES,fill=BOTH)

root.title('gui1g.py')
root.mainloop()
