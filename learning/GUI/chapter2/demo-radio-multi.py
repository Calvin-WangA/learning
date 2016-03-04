'''
Created on 2016年3月4日

@author: CasparWang
'''
# see what happens when some button have same value
from tkinter import *
from parser import STType
root = Tk()
var = StringVar()
for i in range(10):
    rad = Radiobutton(root,text=str(i),variable=var, value=str(i % 3))
    rad.pack(side=LEFT)
var .set('')    # deselect all initally
root.mainloop()