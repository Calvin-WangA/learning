#!/usr/bin/python
'''
Created on 2016年4月18日

@author: CasparWang
'''
"""
Same as fork-server.py, but use the Python signal module to avoid keeping
child zombie processes after they terminate, instead of an explicit reaper
loop before each new connection; SIG_IGN means ignore, and may not work with
SIG_CHLD child exit signal on all platforms; see Linux documentation for more
about the restartability of a socket.accept call interrupted with a signal;
"""

import os, time, sys, signal
from socket import *
myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)
signal.signal(signal.SIGCHLD, signal.SIG_IGN) # avoid child zombie process

def now():
    return time.ctime(time.time())

def handleClient(connection):
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        if not data: break
        reply = 'Echo=>%s at %s' %(data,now())
        connection.send(reply.encode(encoding='utf_8'))
    connection.close()
    os._exit(0)
    
def dispatcher():
    while True:
        connection, address = sockobj.accept()
        print('Server connected by', address, end='')
        print('at', now())
        childPid = os.fork()
        if childPid == 0:
            handleClient(connection)
            
if __name__ == '__main__':
    dispatcher()
