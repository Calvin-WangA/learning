#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月6日

@author: Calvin Wang
'''
"""
display all images in a directory in pop-up window
"""
import sys,os
from tkinter import *
from PIL.ImageTk import PhotoImage

imgdir = 'F:\Python\images'
if len(sys.argv) > 1: imgdir = sys.argv[1]
imgfiles = os.listdir(path=imgdir)   # get files not include directory path.

main = Tk()
main.title('Viewer')
quit = Button(main,text='Quit all',command=main.quit,font=('courier',25))
quit.pack()
savephotos = []

for imgfile in imgfiles:
    imgpath = os.path.join(imgdir,imgfile)
    win = Toplevel()
    win.title(imgfile)
    try:
        imgobj = PhotoImage(file=imgpath)
        Label(win,image=imgobj).pack()
        print(imgpath,imgobj.width(),imgobj.height())
        savephotos.append(imgobj)
    except:
        errmsg = 'skipping %s\n%s' % (imgfile, sys.exc_info()[1])
        Label(win,text=errmsg).pack()
        
if __name__ == '__main__':
    main.mainloop()