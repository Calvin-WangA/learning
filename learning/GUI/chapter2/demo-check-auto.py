'''
Created on 2016年3月4日

@author: CasparWang
'''
# check buttons, the easy way
from tkinter import *

root = Tk()
states = []
for i in range(10):
    var = IntVar
    chk = Checkbutton(root,text=str(i),variable=var)
    chk.pack(side=LEFT)
    states.append(var)
    
root.mainloop()
print([var.get() for var in states])