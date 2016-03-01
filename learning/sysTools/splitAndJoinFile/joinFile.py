#!/usr/bin/python
'''
Created on 2016年2月28日

@author: Calvin Wang
'''
from fileinput import filename
"""
################################################################################
join all part files in a dir created by split.py, to re-create file.
This is roughly like a 'cat fromdir/* > tofile' command on unix, but is
more portable and configurable, and exports the join operation as a
reusable function. Relies on sort order of filenames: must be same
length. Could extend split/join to pop up Tkinter file selectors.
################################################################################
"""

import sys,os

readSize = 1024

def joinFile(fromDir,toFile):
    output = open(toFile,'wb')
    parts = os.listdir(fromDir)
    parts.sort()
    for fileName in parts:
        filePath = os.path.join(fromDir,fileName)
        fileObj = open(filePath,'rb')
        while True:
            fileBytes = fileObj.read(readSize)
            if not fileBytes: break
            output.write(fileBytes)
        fileObj.close()
    output.close()
    
if __name__ == '__main':
    if len(sys.argv) == 2 and sys.argv[-1] == '-help':
        print('Use: join.py [from-dir-name-to-file-name')
    else:
        if len(sys.argv) != 3:
            interactive = True
            fromDir = input('Directory contains part files?')
            toFile = input('Name of file to be recreated?')
        else:
            interactive = False
            fromDir,toFile = sys.argv[1:]
        absfrom,absto = map(os.path.abspath,[fromDir,toFile])
        print('Joining ',absfrom,'to make',absto)
        
        try:
            joinFile(fromDir,toFile)
        except:
            print('Error joining files:')
            print(sys.exc_info()[0],sys.exc_info()[1])
        else:
            print('Joining complete: see',absto)
            
        if interactive: print('Press Enter Key')
        
        