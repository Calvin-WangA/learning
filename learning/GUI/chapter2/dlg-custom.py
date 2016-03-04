'''
Created on 2016年3月3日

@author: CasparWang
'''
import sys
from tkinter import *

makemodal = len(sys.argv) > 1

def dialog():
    win = Toplevel()                                  # make a new window
    Label(win,text='Hard drive reformatted!').pack()  # add a few widgets
    Button(win,text='OK',command=win.quit).pack()     # set destroy callback 
    if makemodal:
        win.focus_set()    # take over input focus
        win.grab_set()     # disable other windows while i'm open
        win.wait_window()  # and wait here until window destroyed
    print('dialog exit')
    
root = Tk()
Button(root,text='popup',command=dialog).pack()
root.mainloop()