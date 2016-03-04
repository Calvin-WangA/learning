'''
Created on 2016年3月4日

@author: CasparWang
'''
from tkinter import *

msg = Message(text="oh by the way, Which one's Pink?")
msg.config(bg='pink',font=('times',16,'italic'))
msg.pack(expand=YES,fill=BOTH)
mainloop()