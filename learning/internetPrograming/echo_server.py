#!/local/bin/python
#coding: utf-8
'''
Created on 2016年4月6日

@author: CasparWang
'''
"""
Server side: open a TCP/IP socket on port, listen for a message from 
client., and send a echo reply; this is a simple one-shot listen/reply
conversation per client, but it goes into an infinite loop to listen for 
more clients as long as this scripts runs; the client may run on 
a remote machine, or on same computer if it uses "localhost" for server
"""
from socket import * 
myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)   # make a TCP socket object
sockobj.bind((myHost, myPort))
sockobj.listen(5)                        # listen, allow 5 pending connects

while True:
    connection, address = sockobj.accept()  # wait for next client connect
    print('Server connected by', address) 
    while True:
        data = connection.recv(1024)     # read next line on client socket
        if not data: break
        connection.send(b'Echo=>' + data)# send a reply line to the client
    connection.close()
    
