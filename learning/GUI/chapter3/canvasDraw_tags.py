#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月11日

@author: CasparWang
'''
"""
add tagged moves with timer.sleep(not widget.after or thread)
time.sleep will not block the GUI event loop while pasuing, but screen 
not redraw utill callback returns or widget.update call; currently running
onMove callback has exclusive attention until it returns: others pause
if press 'r' or 'o' during move;
"""
from tkinter import *
import canvasDraw,time

class CanvasEventsDemo(canvasDraw.CanvasEventsDemo):
    def __init__(self,parent=None):
        canvasDraw.CanvasEventsDemo.__init__(self,parent)
        self.canvas.create_text(100,10, text='press o or r to move shapes')
        self.canvas.master.bind('<KeyPress-o>', self.onMoveOvals)
        self.canvas.master.bind('<KeyPress-r>', self.onMoveRectangles)
        self.kinds = self.create_oval_tagged, self.create_rectangle_tagged
        
    def create_oval_tagged(self,x1,y1,x2,y2):
        objectId = self.canvas.create_oval(x1,y1,x2,y2)
        self.canvas.itemconfig(objectId, tag='ovals', fill='blue')
        
        return objectId
    
    def create_rectangle_tagged(self,x1,y1,x2,y2):
        objectId = self.canvas.create_rectangle(x1,y1,x2,y2)
        self.canvas.itemconfig(objectId, tag='rectangles', fill='red')
        
        return objectId
    
    def onMoveOvals(self, event):
        print('moving ovals')
        self.moveInSquares('ovals')                  # move all tagged ovals
        
    def onMoveRectangles(self,event):
        print('moving rectangles')
        self.moveInSquares('rectangles')
        
    def moveInSquares(self,tag):
        for i in range(5):
            for (diffX, diffY) in [(+20,0),(0,+20),(-20,0),(0,-20)]:
                self.canvas.move(tag, diffX, diffY)
                self.canvas.update()                  #force screen redraw/update
                time.sleep(0.25)                      #pause but don't block GUI
                
if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()