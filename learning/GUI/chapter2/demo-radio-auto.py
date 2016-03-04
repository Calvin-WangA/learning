'''
Created on 2016年3月4日

@author: CasparWang
'''
# radio buttons, the easy way
from tkinter import *

root = Tk()
var = IntVar(0)          # select 0 to start
for i in range(10):
    rad = Radiobutton(root,text=str(i),
                      value=i,variable=var)
    rad.pack(side=LEFT)
    
root.mainloop()
print(var.get())
    