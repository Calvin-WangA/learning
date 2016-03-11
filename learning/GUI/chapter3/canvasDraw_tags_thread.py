#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月11日

@author: CasparWang
'''
"""
similar, but run time.sleep loops in parallel with threads, not after() events
or single active time.sleep loop; because threads run in parallel, this also
allows ovals and rectangles to be moving at the _same_ time and does not require
update calls to refresh the GUI: in fact, calling .update() once made this crash
badly, though some canvas calls must be thread safe or this wouldn't work at all;
"""
from tkinter import *
import canvasDraw_tags
import threading, time

class CanvasEventsDemo(canvasDraw_tags.CanvasEventsDemo):
    def moveEm(self, tag):
        for i in range(5):
            for (diffX, diffY) in [(+20, 0), (0, +20), (-20, 0), (0, -20)]:
                self.canvas.move(tag, diffX, diffY)
                time.sleep(0.25)
    
    def moveInSquares(self, tag):
        moves = threading.Thread(target=self.moveEm,args=(tag,))
        moves.start()
if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()