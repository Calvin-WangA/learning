#!/usr/local/bin/python
"""
################################################################################
tools launcher; uses guimaker templates, guimixin std quit dialog;
I am just a class library: run mytools script to display the GUI;
################################################################################
"""
'''
Created on 2016年3月14日

@author: CasparWang
'''
from tkinter import *
from learning.GUI.chapter4.guimixin import GuiMixin
impimport learning.GUI.chapter5 as guimaker
class ShellGui(GuiMixin,guimaker.GuiMakerWindowMenu):
    def start(self):
        self.setMenuBar()
        self.setToolBar()
        self.master.title("Shell Tools Listbox")
        self.master.iconname("Shell Tools")
        
    def handleList(self, event):
        label = self.listbox.get(ACTIVE)
        self.runCommand(label)
        
    def makeWidgets(self):
        sbar = Scrollbar(self)
        list = Listbox(self, bg='white')
        sbar.config(command=list.yview)
        list.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        list.pack(side=LEFT, expand=YES, fill=BOTH)
        
        for (label, action) in self.fetchCommands():
            list.insert(END, label)
        list.bind('<Double-1>', self.handleList)
        self.listbox = list
        
    def forToolBar(self, label):
        return True;
    
    def setToolBar(self):
        self.toolBar = []
        for (label, action) in self.setCommands():
            if self.forToolBar(label):
                self.toolBar.append(label, action, dict(side=LEFT))
        self.toolBar.append(('Quit', self.quit, dict(side=RIGHT)))
        
    def setMenuBar(self):
        toolEntries = []
        self.menuBar = [
            ('File', 0, [('Quit', -1, self.quit)]), # pull-down name
            ('Tools', 0, toolEntries) # menu items list            
            ]
        for (label, action) in self.fetchCommands():
            toolEntries.append((label, -1, action))
################################################################################
# delegate to template type-specific subclasses
# which delegate to app tool-set-specific subclasses
################################################################################
class ListMenuGui(ShellGui):
    def fetchCommands(self):
        return self.myMenu
    def runCommand(self, cmd):
        for (label, action) in self.myMenu:
            if label == cmd: action()
                
class DictMenuGui(ShellGui):
    def fetchCommands(self):
        return self.myMenu.items()                    
    def runCommand(self, cmd):
        self.myMenu[cmd]()
            
            
            