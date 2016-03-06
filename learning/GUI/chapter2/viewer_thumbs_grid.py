#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月6日

@author: Calvin Wang
'''
"""
same as viewer_thumbs, but uses the grid geometry manager to try to achieve
a more uniform layout; can generally achieve the same with frames and pack
if buttons are all fixed and uniform in size;
"""
import sys,math
from tkinter import *
from PIL.ImageTk import PhotoImage
from viewer_thumbs import makeThumbs,ViewOne

def viewer(imdir,kind=Toplevel,cols=None):
    """
    custom version that uses gridding
    """
    win = kind()
    win.title("Viewer: " + imgdir)
    thumbs = makeThumbs(imgdir)
    if not cols:
        cols = int(math.ceil(math.sqrt(len(thumbs))))         # fixed or N X N
    rownum = 0
    savephotos = []
    while thumbs:
        thumbsrow,thumbs = thumbs[:cols],thumbs[cols:]
        colnum = 0
        for (imgfile,imgobj) in thumbsrow:
            photo = PhotoImage(imgobj)
            link = Button(win,image=photo)
            handler = lambda savefile = imgfile: ViewOne(imgdir,savefile)
            link.config(command=handler,width=100,height=100)
            link.grid(row=rownum,column=colnum)
            savephotos.append(photo)
            colnum += 1
        rownum += 1
    Button(win,text='Quit',command=win.quit).grid(columnspan=cols,stick=NW)
    return win,savephotos

if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or 'F:\Python\images'
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()