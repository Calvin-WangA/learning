#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月15日

@author: Calvin Wang
'''
# GUI that displays data produced and queued by worker threads(class-based)
import threading, queue, time
from tkinter.scrolledtext import ScrolledText

class ThreadGui(ScrolledText):
    threadPerClick = 4
    
    def __init__(self, parent=None):
        ScrolledText.__init__(self, parent)
        self.pack()
        self.dataQueue = queue.Queue()
        self.bind('<Button-1>', self.makeThreads)
        self.consumer()
        
    def producer(self, id):
        for i in range(5):
            time.sleep(0.5)
            self.dataQueue.put('[producer id=%d, count=%d]' %(id, i))
            
    def consumer(self):
        try:
            data = self.dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            self.insert('end', 'consumer got => %s\n' %str(data))
            self.see('end')
        self.after(100, self.consumer)
        
    def makeThreads(self, event):
        for i in range(self.threadPerClick):
            thread = threading.Thread(target=self.producer, args=(i,))
            thread.start()
            
if __name__ == '__main__':
    root = ThreadGui()
    root.mainloop()
            