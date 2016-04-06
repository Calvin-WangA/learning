#!usr/local/bin/python
#coding:utf-8
'''
Created on 2016年3月18日

@author: CasparWang
'''
from tkinter import *
from learning.GUI.chapter5.operateFile import *
class PyEdit(Frame):
    
    text = Text(relief=SUNKEN)
    text.insert(END, "HELLO CLIPBORD")
    menuBars =  [('file',[('new', quit),('open',quit)
                         ,('save', quit),('save as', quit)])
                 ,('edit',[('draw',quit),('event',[('click',quit)
                                                   ,('double click', quit)])])
                ]
    
    toolBars = [('cut',quit),('copy', lambda text: copyText(text)),('paste',quit)]
        
    def __init__(self, parent=None):
        
        Frame.__init__(self, parent);
        self.config(width=600, height=400)
        self.pack(expand=YES, fill=BOTH)
        self.makeMenuBars()
        self.makeEditArea()
        self.makeToolBars()
        
        
    def makeMenuBars(self):
        self.rootMenu = Menu(self.master)
        self.master.config(menu=self.rootMenu)
        
        for (name, items) in self.menuBars:
            menu = Menu(self.rootMenu)
            self.rootMenu.add_cascade(label=name, menu=menu)
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
        self.master.toolbar = Frame(self.master)
        for (name, func) in self.toolBars:
            button = Button(self.master.toolbar,text=name, command=func)
            button.pack(side=LEFT)
        self.master.toolbar.pack(side=BOTTOM, fill=X)
            
    def makeEditArea(self):
        yscroll = Scrollbar(self.master)
        xscroll = Scrollbar(self.master, orient='horizontal')
       
        self.text.config(yscrollcommand=yscroll.set)
        self.text.config(xscrollcommand=xscroll.set)
        yscroll.config(command=self.text.yview)
        xscroll.config(command=self.text.xview)
        yscroll.pack(side=RIGHT, fill=Y)
        xscroll.pack(side=BOTTOM, fill=X)
        self.text.config(bg='pink')
        self.text.pack(side=TOP, expand=YES, fill=BOTH)
        
        
if __name__ == '__main__':
    PyEdit().mainloop()
        
