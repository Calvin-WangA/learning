#!/usr/local/bin/python
'''
Created on 2016年4月18日

@author: CasparWang
'''
"""
Server side: open a socket on a port, listen for a message from a client,
and send an echo reply; forks a process to handle each client connection;
child processes share parent's socket descriptors; fork is less portable
than threads--not yet on Windows, unless Cygwin or similar installed;
"""

import os, time, sys
from socket import *

myHost = ''
myPort = 50007

sockobj = socket(AF_INET,SOCK_STREAM)
sockobj.bind((myHost,myPort))
sockobj.listen(5)                     # allow five pending connection

def now():                            # current time on Server
    return time.ctime(time.time())

activeChildren = []
def reapChildren():                   # reap any dead child processes
    while activeChildren:
        pid, stat = os.waitpid(0, os.WNOHANG) # don't hang if no child existed
        if not pid:break;
        activeChildren.remove(pid)
        
def handleClient(connection):
    time.sleep(5)                     # simulate a blocking activity
    while True:
        data = connection.recv(1024)  # till eof when socket close
        if not data: break
        reply = 'Echo=>%s at %s' %(data, now())
        connection.send(reply.encode(encoding='utf_8'))
    connection.close()
    os._exit(0)

def dispatcher():
    while True:                       # listen until process killed
        connection, address = sockobj.accept()
        print('Server connected by', address, end='')
        print('at', now())
        reapChildren()
        childPid = os.fork()
        if childPid == 0:
            handleClient(connection)
        else:
            activeChildren.append(childPid)
            
if __name__ == '__main__':
    dispatcher()
            
            
    
    
    
    
    
    