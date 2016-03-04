'''
Created on 2016年3月4日

@author: CasparWang
'''
# can fetch values after destroy with stringvars

from tkinter import *
from entry3 import makeForm,fetch,fields

def show(variables,popup):
    popup.destroy()
    fetch(variables)                      # variables live on after window destroyed

def ask():
    popup = Toplevel()
    vars = makeForm(root,fields)
    Button(popup,text='OK',command=(lambda: show(vars,popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()
    
root = Tk()
Button(root,text='Dialog',command=ask).pack()
root.mainloop()