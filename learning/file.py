'''
Created on 2016年2月26日

@author: CasparWang
'''
import sys
from os import walk,path

def show(path):
    allSizes = []
    for (thisDir,subDirs,thisFiles) in walk(path):
        for file in thisFiles:
            if file.endswith('.py'):
                fullPath = thisDir + "/"+file
                print("path = ",fullPath)
                fileSize = path.getsize(fullPath)
                allSizes.append((fileSize,fullPath))
                
    allSizes.sort()
    
    return allSizes
if __name__ == '__main__':
    results = show('E:/PythonPractise');
    print(results[:2])
    print(results[-2:])