#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月9日

@author: CasparWang
'''
"demo advanced tag and text interfaces"

from tkinter import *
from PIL.ImageTk import PhotoImage
from PIL import Image
root = Tk()
def hello(event):
    print('Got tag event')
    
#make and config a text
text =Text()
text.config(font=('courier', 15, 'normal'))
text.config(width=20,height=12)
text.pack(expand=YES, fill=BOTH)
text.insert(END,'This is\n\nthe meaning\n\nof life.\n\n')

#embed windows and photo
btn = Button(text,text='Spam', command=lambda: hello(0))
btn.pack()
text.window_create(END,window=btn)
text.insert(END, '\n\n')
imgobj = Image.open('./MIMI.jpg')
imgobj.thumbnail((100,100),Image.ANTIALIAS)
imgobj.save('./thumbs/mimi.jpg')
img = PhotoImage(file='./thumbs/mimi.jpg')
text.image_create(END,img)

#apply tags to substrings
text.tag_add('demo','1.5','1.7')
text.tag_add('demo','3.0','3.3')
text.tag_add('demo','5.3','5.7')
text.tag_config('demo',backgound='purple')
text.tag_config('demo',foreground='white')
text.tag_add('demo', font=('times',16,'underline'))
text.tag_bind('demo', '<Double-1>', hello)
root.mainloop()