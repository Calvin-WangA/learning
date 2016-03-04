'''
Created on 2016年3月4日

@author: CasparWang
'''
# hold on to your radio variables(an obscure thing, indeed)
from tkinter import *
root = Tk()

def radio1():             # local vars are temporary
    global tmp        # make it global fixs problem 
    tmp = IntVar()
    for i in range(10):
        rad = Radiobutton(root,text=str(i),value=i,variable=tmp)
        rad.pack(side=LEFT)
        
    tmp.set(5)  # select 6th button
    
radio1()
root.mainloop()
    