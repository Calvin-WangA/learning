'''
Created on 2016年2月28日

@author: Calvin Wang
'''
"""
Find the largest file of a given type in an arbitrary directory tree.
Avoid repeat paths, catch errors, add tracing and line count size.
Also uses sets, file iterators and generator to avoid loading entire
file, and attempts to work around undecodable dir/file name prints.
"""

import os,pprint
from sys import argv,exc_info

trace = 1
dirName = os.curdir
extName = '.py'

if len(argv) > 1: dirName = argv[1]
if len(argv) > 2: extName = argv[2]
if len(argv) > 3: trace = int(argv[3]) # ext: '..py'

def tryPrint(arg):
    try:
        print(arg)
    except UnicodeDecodeError:
        print(arg.encode())  # try raw byte string
        
def scanDirTree():
    visited = set()
    allSizes = []
    
    for (thisDir,subHeres,thisHeres) in os.walk(dirName):
        if trace: tryPrint(thisDir)
        thisDir = os.path.normpath(thisDir)
        fixName = os.path.normcase(thisDir)
        if fixName in visited:
            if trace: tryPrint('skipping' + thisDir)
        else:
            visited.add(fixName)
            for fileName in thisHeres:
                if fileName.endswith(extName):
                    if trace > 1: tryPrint('+++' + fileName)
                fullName = os.path.join(thisDir,fileName)
                try:
                    bytesize = os.path.getsize(fullName)
                    linesize = sum(+1 for line in open(fullName,'r'))
                except Exception:
                    print('error',exc_info()[0])
                else:
                    allSizes.append((bytesize,linesize,fullName))
    
    return allSizes
                                    
if __name__ == '__main__':
    allSizes = scanDirTree()
    for (title, key) in [('bytes',0),('lines',1)]:
        print('\nBye %s ...' %title)
        allSizes.sort(key= lambda x: x[key])
        pprint.pprint(allSizes[:3])
        pprint.pprint(allSizes[-3:])