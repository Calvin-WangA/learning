'''
Created on 2016年2月26日

@author: CasparWang
'''
import sys,os

def show(path):
    allSizes = []
    for (thisDir,subDirs,thisFiles) in os.walk(path):
        for file in thisFiles:
            if file.endswith('.py'):
                fullPath = os.path.join(thisDir,file)
                print("path = ",fullPath)
                fileSize = os.path.getsize(fullPath)
                allSizes.append((fileSize,fullPath))
                
    allSizes.sort()
    
    return allSizes
if __name__ == '__main__':
    results = show('F:/Python');
    print(results[:2])
    print(results[-2:])