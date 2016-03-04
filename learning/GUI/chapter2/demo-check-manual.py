'''
Created on 2016年3月4日

@author: CasparWang
'''
# check buttons, the hard way(without variables)
from tkinter import *
states = []
def onPress(i):
    states[i] = not states[i]
    
root = Tk()
for i in range(10):
    chk = Checkbutton(root,text=str(1),command=(lambda i = i: onPress(i)))
    chk.pack(side=LEFT)
    states.append(False)
    
root.mainloop()
print(states) 