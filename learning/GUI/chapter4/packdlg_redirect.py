#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月14日

@author: CasparWang
'''
# wrap command-line script in GUI redirection tool to pop up its output
from tkinter import *
from learning.GUI.chapter4.packdlg import runPackDialog
from learning.GUI.chapter4.guiStreams import redirectedGuiFunc

def runPackDialog_Wrapped():
    redirectedGuiFunc(runPackDialog)
    
if __name__ == '__main__':
    root = Tk()
    Button(root, text='pop', command=runPackDialog_Wrapped()).pack(fill=X)
    root.mainloop()
