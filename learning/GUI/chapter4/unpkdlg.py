#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月14日

@author: CasparWang
'''
#popup a GUI dialog for unpacker scripter arguments, and run it
from tkinter import *
from learning.GUI.chapter4.unpacker import unpack
from learning.GUI.chapter4.formrows import makeFormRow

def unpackDialog():
    win = Toplevel()
    win.title('Enter Unpack Parameters')
    var = makeFormRow(win, label='Input file', width=11)
    win.bind('<Key-Return>', lambda event: win.destroy())
    win.grab_set()
    win.focus_set()
    win.wait_window()
    return var.get()

def runUnpackDialog():
    input = unpackDialog()
    if input != '':
        print('Unpacker: ',input)
        unpack(ifile=input, prefix='')
        
if __name__ == '__main__':
    Button(None, text='Popup', command=runUnpackDialog).pack()
    mainloop()