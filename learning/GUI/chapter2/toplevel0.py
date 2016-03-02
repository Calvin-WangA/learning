'''
Created on 2016年3月2日

@author: CasparWang
'''
import sys
from tkinter import Toplevel,Button,Label

win1 = Toplevel()
win2 = Toplevel()

Button(win1,text='Spam',command=sys.exit).pack()
Button(win2,text="SPAM",command=sys.exit).pack()

Label(text='Popus').pack()
win1.mainloop()