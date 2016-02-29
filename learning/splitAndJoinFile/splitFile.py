#!/usr/bin/python
'''
Created on 2016年2月28日

@author: Calvin Wang
'''
"""
################################################################################
split a file into a set of parts; join.py puts them back together;
this is a customizable version of the standard Unix split command-line
utility; because it is written in Python, it also works on Windows and
can be easily modified; because it exports a function, its logic can
also be imported and reused in other applications;
################################################################################
"""

import sys,os

kilobytes = 1024
megaBytes = kilobytes * 1000
chunkSize = int(1.4 * megaBytes)  # default: a rougly floppy

def split(fromFile,toDir,chunkSize = chunkSize):
    if not os.path.exists(toDir):
        os.mkdir(toDir)
    else:
        for fname in os.listdir(toDir):
            os.remove(os.path.join(toDir,fname))
            
    partNum = 0
    inFile = open(fromFile,'rb')
    while True:
        chunk = inFile.read(chunkSize) #get next part <= chunkSize
        if not chunk: break
        partNum += 1
        fileName = os.path.join(toDir,('part%04d' %partNum))
        fileobj = open(fileName,'wb')
        fileobj.write(chunk)
        fileobj.close()
        
    inFile.close()
    assert partNum <= 9999  # join sort fails if 5 digits
    return partNum
           
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: split.py [file to split target-dir [chunksize]')
    else:
        if len(sys.argv) < 3:
            interactive = True
            fromFile = input('File to be split?')  # input if clicked
            toDir = input('Directory to store part files?')
        else:
            interactive = False
            fromFile,toDir = sys.argv[1:3]  # args in cmdline
            if len(sys.argv) == 4: chunkSize = int(sys.argv[3])
        absfrom, absto = map(os.path.abspath,[fromFile,toDir])
        print('Splitting ',absfrom,'to ',absto,'by ',chunkSize)
        
        try:
            parts = split(fromFile,toDir,chunkSize)
        except: 
            print('Error during split:')
            print(sys.exc_info()[0],sys.exc_info()[1])
        else:
            print('Split finished:',parts,'parts are in ',absto)
            
        if interactive: input('Press Enter Key') #pause id clicked            