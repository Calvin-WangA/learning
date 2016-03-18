#!usr/local/bin/python
#coding:utf-8
'''
Created on 2016年3月18日

@author: CasparWang
'''
from tkinter import *

class PyEdit(Frame):
    
    menuBars =  [('file',[('new', quit),('open',quit)
                         ,('save', quit),('save as', quit)])
                 ,('edit',[('draw',quit),('event',[('click',quit)
                                                   ,('double click', quit)])])
                ]
    
    toolBars = [('cut',quit),('copy',quit),('paste',quit)]
    
    def __init__(self, parent=None):
        Frame.__init__(self, parent);
        self.config(width=600, height=400)
        self.pack(expand=YES, fill=BOTH)
        self.makeMenuBars()
        self.makeToolBars()
        self.makeWidgets()
        
    def makeMenuBars(self):
        rootMenu = Menu(self.master)
        self.master.config(menu=rootMenu)
        
        for (name, items) in self.menuBars:
            menu = Menu(rootMenu)
            rootMenu.add_cascade(label=name, menu=menu)
            self.addMenuItems(menu, items)
    
    def addMenuItems(self,menu, items):
        for item in items:
            if type(item[1]) != list:
                menu.add_command(label=item[0], command=item[1])
            else:
                subMenu = Menu(menu)
                menu.add_cascade(label=item[0], menu=subMenu)
                self.addMenuItems(subMenu,item[1])
               
    def makeToolBars(self):
        toolbar = Frame(self)
        for (name, func) in self.toolBars:
            button = Button(toolbar,text=name, command=func)
            button.pack(side=LEFT)
        toolbar.pack(side=BOTTOM, fill=X)
            
    def makeWidgets(self):
        yscroll = Scrollbar(self)
        xscroll = Scrollbar(self, orient='horizontal')
        self.text = Text(self,relief=SUNKEN)
        self.text.config(yscrollcommand=yscroll.set)
        self.text.config(xscrollcommand=xscroll.set)
        yscroll.config(command=self.text.yview)
        xscroll.config(command=self.text.xview)
        yscroll.pack(side=RIGHT, fill=Y)
        xscroll.pack(side=BOTTOM, fill=X)
        self.text.pack(side=TOP, expand=YES, fill=BOTH)
        
        
if __name__ == '__main__':
    PyEdit().mainloop()
        
