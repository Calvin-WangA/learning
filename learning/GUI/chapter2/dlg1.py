'''
Created on 2016年3月3日

@author: CasparWang
'''
from tkinter import *
from tkinter.messagebox import *

def callback():
    if askyesno('Verify','Do you really want to quit?'):
        showwarning('Yes','Quit not yet implemented')
    else:
        showinfo('No','Quit has been cancelled')
        
errmsg = 'Sorry, no Spam allowed!'
Button(text="Quit",command=callback).pack(fill=X)
Button(text='Cancell',command=lambda: showerror('Spam', errmsg)).pack(fill=X)
mainloop()