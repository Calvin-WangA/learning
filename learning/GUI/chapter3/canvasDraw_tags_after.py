#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月11日

@author: CasparWang
'''
from tkinter import mainloop
"""
similar, but with widget.after() scheduled events, not time.sleep loops;
because these are scheduled events, this allows both ovals and rectangles
to be moving at the _same_ time and does not require update calls to refresh
the GUI; the motion gets wild if you press 'o' or 'r' while move in progress:
multiple move updates start firing around the same time;
"""
from tkinter import *
import canvasDraw_tags

class CanvasEventsDemo(canvasDraw_tags.CanvasEventsDemo):
    def moveEm(self, tag, moremoves):
        (diffX, diffY), moremoves = moremoves[0],moremoves[1:]
        self.canvas.move(tag, diffX, diffY)
        if moremoves:
            self.canvas.after(250, self.moveEm, tag, moremoves)
            
    def moveInSquares(self, tag):
        allmoves = [(+20, 0), (0, +20), (-20, 0), (0, -20)] * 5
        self.moveEm(tag, allmoves)
        
if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()