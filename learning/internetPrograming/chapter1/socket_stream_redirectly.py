#!/usr/bin/python
'''
Created on 2016年4月19日

@author: CasparWang
'''
from learning.internetPrograming.chapter1.select_server import reply
import socket
"""
###############################################################################
Tools for connecting standard streams of non-GUI programs to sockets that
a GUI (or other) program can use to interact with the non-GUI program.
###############################################################################
"""

import sys
from socket import *
port = 50008
host = 'localhost'

def initListenerSocket(port=port):
    """
    initialize connected socket for callers that listen in server mode
    """
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    conn, addr = sock.accept()
    return conn

def redirectOut(port=port, host=host):
    """
    connect caller's standard stream to a socket for GUI to listen 
    start caller after listener started, else connect fails before accept
    """
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host,port))
    file = sock.makefile('w')
    sys.stdout = file
    
    return sock

def redirectIn(port=port, host=host):
    """
    connect caller's standard input stream to a sockt for GUI to provide
    """
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host,port))
    file = sock.makefile('r')
    sys.stdin = file
    
    return sock

def redirectBothAsClient(port=port, host=host):
    """
    connect caller's standard input and output stream to same socket
    in this mode, caller a client to a server: sends msg, receives reply
    """
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    ifile = sock.makefile('r')
    wfile = sock.makefile('w')
    sys.stdin = ifile
    sys.stdout = wfile
    
    return sock

def redirectBothAsServer(port=port, host=host):
    """
    connect caller's standard input and output stream to same socket
    in this mode, caller is server to a client: receives msg, send reply
    """
    sock = socket(AF_INET,SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    conn, addr = sock.accept()
    ifile = conn.makefile('r')
    wfile = conn.makefile('w')
    sys.stdin = ifile
    sys.stdout = wfile
    
    return conn
