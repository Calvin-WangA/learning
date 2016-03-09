#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月9日

@author: CasparWang
'''
"""
image viewer extension: uses fixed-size thumbnail buttons for uniform layout, and
adds scrolling for large image sets by displaying thumbs in a canvas widget with
scroll bars; requires PIL to view image formats such as JPEG, and reuses thumbs
maker and single photo viewer in viewer_thumbs.py; caveat/to do: this could also
scroll popped-up images that are too large for the screen, and are cropped on
Windows as is; see PyPhoto later in Chapter 11 for a much more complete version;
"""
import sys, math
from tkinter import *
from PIL.ImageTk import PhotoImage
from chapter2.view_thumbs import makeThumbs,ViewOne 
#makeThumbs, ViewOne

def viewer(imgdir, kind=Toplevel, numcols=None, height=300,width=300):
    """
    use fixed-size buttons, scrollable canvas;
    sets scrollable(full) size, and places thumbs at absolute x, y
    corrdinates in canvas; caveat: assumes all thumbs are same size 
    """
    win = kind()
    win.title('Simple Viewer: ' + imgdir)
    quit = Button(win, text='Quit', command=win.quit, bg='beige')
    quit.pack(side=BOTTOM, fill=X)
    
    canvas = Canvas(win, borderwidth=0)
    vbar = Scrollbar(win)
    hbar = Scrollbar(win, orient='horizontal')

    vbar.pack(side=RIGHT, fill=Y)
    hbar.pack(side=BOTTOM, fill=X)
    canvas.pack(side=TOP, expand=YES, fill=BOTH)
    
    vbar.config(command=canvas.yview)
    hbar.config(command=canvas.xview)
    canvas.config(yscrollcommand=vbar.set)
    canvas.config(xscrollcommand=hbar.set)
    canvas.config(width=height, height=height)
    
    thumbs = makeThumbs(imgdir)
    numthumbs = len(thumbs)
    if not numcols:
        numcols = int(math.ceil(math.sqrt(numthumbs)))
    numrows = int(math.ceil(numthumbs/numcols))
    
    linksize = max(thumbs[0][1].size)                      #width, height
    fullsize = (0,0,                                       #upper left x, y
                (linksize*numcols),(linksize*numrows))     #lower right x,y
    canvas.config(scrollregion=fullsize)
    
    rowpos = 0
    savephotos = []
    while thumbs:
        thumbsrow, thumbs = thumbs[:numcols],thumbs[numcols:]
        colpos = 0
        for (imgfile, imgobj) in thumbsrow:
            photo = PhotoImage(imgobj)    
            link = Button(canvas, image=photo)
            handler = lambda savefile = imgfile: ViewOne(imgdir,savefile)
            link.config(command=handler, width=linksize, height=linksize)
            link.pack(side=LEFT, expand=YES)
            canvas.create_window(colpos,rowpos, anchor=NW,
                                 window=link, width=linksize, height=linksize)
            colpos += linksize
            savephotos.append(photo)
        rowpos += linksize
    
    return win, savephotos

if __name__ == '__main__':
    imgdir = '' if len(sys.argv) < 2 else sys.argv[1]
    main, save = viewer(imgdir,kind=Tk)
    main.mainloop()