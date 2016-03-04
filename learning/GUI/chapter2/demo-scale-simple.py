'''
Created on 2016年3月4日

@author: CasparWang
'''
from tkinter import *

root = Tk()
scl = Scale(root,from_=-100, to=100,tickinterval=10,resolution=10)
scl.pack(expand=YES, fill=Y)

def report():
    print(scl.get())

Button(root,text='state',command=report).pack(side=LEFT)

if __name__ == '__main__':
    root.mainloop()