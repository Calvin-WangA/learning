#!/usr/bin/python
'''
Created on 2016年4月18日

@author: CasparWang
'''
"""
Server side: open a socket on a port, listen for a message from a client, and
send an echo reply; this version uses the standard library module socketserver to
do its work; socketserver provides TCPServer, ThreadingTCPServer, ForkingTCPServer,
UDP variants of these, and more, and routes each client connect request to a new
instance of a passed-in request handler object's handle method; socketserver also
supports Unix domain sockets, but only on Unixen; see the Python library manual.
"""

import socketserver, time
myHost = ''
myPort = 50007

def now():
    return time.ctime(time.time())

class MyClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address, now())
        time.sleep(5)
        while True:
            data = self.request.recv(1024)
            reply = 'Echo=>%s at %s' %(data, now())
            self.request.send(reply.encode())
            if not data: break
        self.request.close()
   
if __name__ == '__main__':
    # make a threaded server, listen/handle clients forever
    myaddr = (myHost, myPort)
    server = socketserver.ThreadingTCPServer(myaddr,MyClientHandler)
    server.serve_forever()