#!/usr/bin/python
'''
Created on 2016年4月18日

@author: CasparWang
'''
from _multiprocessing import send
"""
Server side: open a socket on a port, listen for a message from a client,
and send an echo reply; echoes lines until eof when client closes socket;
spawns a thread to handle each client connection; threads share global
memory space with main thread; this is more portable than fork: threads
work on standard Windows systems, but process forks do not;
"""
import time, threading as thread
from socket import *
myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)

def now():
    return time.ctime(time.time())

def handleClient(connection):
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        reply = 'Echo->%s at %s' %(data, now())
        connection.send(reply.encode())
        if not data: break;
    connection.close()
    
def dispatcher():
    while True:
        connection, address = sockobj.accept()
        print('Server connected by ', address, end='')
        print('at', now())
        thread.Thread(target=handleClient
                      , args=(connection,)).start()
        
if __name__ == '__main__':
    dispatcher()