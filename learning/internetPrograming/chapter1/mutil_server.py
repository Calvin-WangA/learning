#!/usr/bin/python
'''
Created on 2016年4月18日

@author: CasparWang
'''
import os, time, signal
from multiprocessing import Process
from socket import *
myHost = ''
myPort = 50007

def now():                            # current time on Server
    return time.ctime(time.time())

activeChildren = []
def reapChildren():                   # reap any dead child processes
    while activeChildren:
        pid, stat = os.waitpid(0, os.WNOHANG) # don't hang if no child existed
        if not pid:break;
        activeChildren.remove(pid)
        
def handleClient(connection):
    print('Child:', os.getpid())
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        reply = 'Echo=>%s at %s' %(data, now())
        connection.send(reply.encode())
        if not data: break
    connection.close()
    os._exit(0)
    
def dispatcher():
    while True:
        connection, address = sockobj.accept()
        print('Server connected by ', address, end='')
        print('at', now())
        Process(target=handleClient, args=(connection,)).start()
        
if __name__ == '__main__':
    print('Parent:', os.getpid)
    sockobj = socket(AF_INET,SOCK_STREAM)
    sockobj.bind((myHost, myPort))
    sockobj.listen(5)
    dispatcher()