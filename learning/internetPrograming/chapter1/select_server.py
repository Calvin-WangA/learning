#!/usr/bin/python
'''
Created on 2016年4月18日

@author: CasparWang
'''
"""
Server: handle multiple clients in parallel with select. use the select
module to manually multiplex among a set of sockets: main sockets which
accept new client connections, and input sockets connected to accepted
clients; select can take an optional 4th arg--0 to poll, n.m to wait n.m
seconds, or omitted to wait till any socket is ready for processing.
"""

import sys, time
from select import select
from socket import socket, AF_INET, SOCK_STREAM

def now():
    return time.ctime(time.time())

myHost = ''
myPort = 50007
if len(sys.argv) == 3:
    myHost, myPort = sys.argv[1:]
numPortSocks = 2

# make main sockets for accepting new client requests
mainsocks, readsocks, writesocks = [], [] ,[]
for i in range(numPortSocks):
    portsock = socket(AF_INET,SOCK_STREAM) 
    portsock.bind((myHost, myPort))
    portsock.listen(5)
    mainsocks.append(portsock)
    readsocks.append(portsock)
    myPort += 1
    
# event loop: listen and multiplex until server process killed
print('select-server loop starting')
while True:
    #print(readsocks)
    readables, writeables, axceptions = select(readsocks,writesocks,[])
    for sockobj in readsocks:
        if sockobj in mainsocks:
            # port socket: accept new client
            newsock, address = sockobj.accept()
            print('Connect: ', address, id(newsock))
            readsocks.append(newsock)
        else:
            # client socket: read next line
            data = sockobj.recv(1024)
            print('\tgot', data, 'on', id(sockobj))
            if not data:
                sockobj.close()
                readsocks.remove(sockobj)
            else:
                # this may block: should really select for writes too
                reply = 'Echo=>%s at %s' %(data, now())
                sockobj.send(reply.encode())
