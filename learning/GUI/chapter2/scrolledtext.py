#！usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月8日

@author: Calvin Wang
'''
"a simple text or file viewer component."

print("PP4E scrolledtext")
from tkinter import *

class ScrolledText(Frame):
    def __init__(self,parent=None, text='', file=None):
        Frame.__init__(self,parent)
        self.pack(expand=YES, fill=BOTH)
        self.makeWidgets()
        self.setText(text,file)
        
    def makeWidgets(self):
        sbar = Scrollbar(self)
        text = Text(self,relief=SUNKEN)
        sbar.config(command=text.yview)
        text.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT, expand=YES, fill=BOTH)
        self.text = text
    
    def setText(self, text='', file=None):
        if file:
            text = open(file,'r').read()
            
        self.text.delete('1.0',END)             # delete current text
        self.text.insert('1.0',text)            # add at line 1, col 0
        self.text.mark_set(INSERT,'1.0')        # set insert cursor
        self.text.focus()
        
    def getText(self):
        return self.text.get('1.0', END+ '-1C') 
    
if __name__ == "__main__":
    root = Tk()
    if len(sys.argv) > 1:
        st = ScrolledText(file=sys.argv[1])
    else:
        st = ScrolledText(text="Words\ngo here")
        
    def show(event):
        print(repr(st.getText))
        
    root.bind('<Key-Escape>', show)
    root.mainloop()
               