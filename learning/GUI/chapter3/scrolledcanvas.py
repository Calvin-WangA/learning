#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月9日

@author: CasparWang
'''
"a simple vertically-scrollable canvas component and demo"
from tkinter import *

class ScrolledCanvas(Frame):
    def __init__(self, parent=None, color='brown'):
        Frame.__init__(self,parent)
        self.pack(expand=YES, fill=BOTH)
        canv = Canvas(self,bg=color,relief=SUNKEN)
        canv.config(width=300, height=200)
        canv.config(scrollregion=(0,0,300,1000))      # canvas size corners
        canv.config(highlightthickness=0)             #no pixels to border
        
        sbar = Scrollbar(self)
        sbar.config(command=canv.yview)
        canv.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        canv.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.fillContent(canv)
        canv.bind('<Double-1>', self.onDoubleClick)   # set event handler
        self.canv = canv
        
    def fillContent(self,canv):
        for i in range(10):
            canv.create_text(150, 50 + (i*100), text='spam' + str(i), fill='beige')
            
    def onDoubleClick(self,event):
        print(event.x,event.y)
        print(self.canv.canvasx(event.x), self.canv.canvasy(event.y))
        
if __name__ == '__main__':
    ScrolledCanvas().mainloop()
        
        