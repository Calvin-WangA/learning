#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月15日

@author: Calvin Wang
'''
# GUI displayed data produced and queued by worker threads
from threading import Thread
import queue, time

dataQueue = queue.Queue()        # infinite size

def producer(id):
    for i in range(5):
        time.sleep(0.1)
        print('Put')
        dataQueue.put('[producer id=%d, count=%d]' %(id, i))
        
def consumer(root):
    try:
        print('get')
        data = dataQueue.get(block=False)
    except queue.Empty:
        pass
    else:
        root.insert('end', 'consumer got => %s\n' %str(data))
        root.see('end')
    root.after(250, lambda: consumer(root))    # 4 times per sec
    
def makeThreads():
    for i in range(4):
        thread = Thread(target=producer, args=(i,))
        thread.start()
        
if __name__ == '__main__':
    # main GUI thread: spawn batch of worker threads on each mouse click
    from tkinter.scrolledtext import ScrolledText
    root = ScrolledText()
    root.pack()
    root.bind('<Button-1>', lambda event: makeThreads())
    consumer(root)                   # start queue check loop in main thread
    root.mainloop()                
    