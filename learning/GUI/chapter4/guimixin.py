#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月12日

@author: Calvin Wang
'''

"""
###############################################################################
a "mixin" class for other frames: common methods for canned dialogs,
spawning programs, simple text viewers, etc; this class must be mixed
with a Frame (or a subclass derived from Frame) for its quit method
###############################################################################
"""

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from learning.GUI.chapter3.scrolledtext import ScrolledText

class GuiMixin:
    def infobox(self,title, text):
        return showinfo(title, text)
    
    def errorbox(self, text):
        return showerror("Error!", text)
    
    def question(self, title, text):
        return askyesno(title, text)
    
    def notdone(self):
        showerror('Not implemented', 'Option not available')
        
    def quit(self):
        ans = self.question('Verify quit', 'Are you sure you want to quit?')
        if ans:
            Frame.quit(self)
            
    def help(self):
        self.infobox('RTEM', 'See Figure 1...')
        
    def selectOpenFile(self, file="", dir="."):
        return askopenfilename(initialdir=dir, inittialfile=file) 
    
    def selectSaveFile(self, file="", dir="."):
        return asksaveasfilename(initialdir=dir, initialfile=file)
    
    def clone(self, args=()):
        new = Toplevel()           # make new in-process version of me
        myClass = self.__class__   # instance's(lowest) class object
        myClass(new, *args)        # attach/run instance to new window
        
    def spawn(self, pycmdline, wait=False):
        if not wait:                        # start new progress
                                            # run Python program
        else:
            System(pycmdline, pycmdline)()  # wait for it to exit 
            
    def browser(self, filename):
        new =Toplevel()
        view = ScrolledText(new, file=filename)
        view.text.config(width=85, height=30)
        view.text.config(font=('courier',10,'normal'))
        new.title('Text Viewer')
        new.iconname('browser')
        
    """
    def browser(self, filename): # if tkinter.scrolledtext
        new = Toplevel() # included for reference
        text = ScrolledText(new, height=30, width=85)
        text.config(font=('courier', 10, 'normal'))
        text.pack(expand=YES, fill=BOTH)
        new.title("Text Viewer")
        new.iconname("browser")
        text.insert('0.0', open(filename, 'r').read() )
    """
            
if __name__ == '__main__':
    class TestMixin(GuiMixin,Frame):
        def __init__(self, parent=None):
            Frame.__init__(self,parent)
            self.pack()
            Button(self, text='quit', command=self.quit).pack(fill=X)
            Button(self, text='help', command=self.help).pack(fill=X)
            Button(self, text='clone', command=self.clone).pack(fill=X)
            Button(self, text='spawn', command=self.other).pack(fill=X)  
            
        def other(self):
            self.spawn('guimixin.py')  # spawn self as separate process
            
    TestMixin().mainloop()