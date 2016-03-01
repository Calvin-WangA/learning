'''
Created on 2016年2月29日

@author: CasparWang
'''
"""
################################################################################
Usage: "python cpall.py dirFrom dirTo".
Recursive copy of a directory tree. Works like a "cp -r dirFrom/* dirTo"
Unix command, and assumes that dirFrom and dirTo are both directories.
Was written to get around fatal error messages under Windows drag-and-drop
copies (the first bad file ends the entire copy operation immediately),
but also allows for coding more customized copy operations in Python.
################################################################################
"""

import sys, os

maxfileload = 1000000
blksize = 1024 * 500

def copyFile(pathFrom, pathTo,maxfileload=maxfileload):
    """
    copy one file pathFrom to pathTo, byte for byte;
    use binarys file modes to supress Unicode decode and endline transform
    """
    if os.path.getsize(pathFrom) <= maxfileload:
        bytesFrom = open(pathFrom,'rb')
        open(pathTo,'wb').write(bytesFrom)
    else:
        fileFrom = open(pathFrom,'rb')
        fileTo = open(pathTo,'wb')
        while True:
            bytesFrom = fileFrom.read(blksize)
            if not bytesFrom: break
            fileTo.write(bytesFrom)
            
def copyTree(dirFrom,dirTo,verbose=0):
    """
    Copy contents of dirFrom and below to dirTo ,return(files,dirs) counts;
    may needs to use bytes for dirnames if undecodable on other platforms;
    may need to do more file type checking on Unix: skip links,fifos,etc.
    """
    fcount = dcount = 0
    for filename in os.listdir(dirFrom):
        pathFrom = os.path.join(dirFrom,filename)
        pathTo = os.path.join(dirTo,filename)
        if not os.path.isdir(pathFrom):
            try:
                if verbose > 1: print('copying',pathFrom,'to',pathTo)
                copyFile(pathFrom,pathTo)
                fcount += 1
            except:
                print('Error copying',pathFrom,'to',pathTo,'--skipped')
                print(sys.exc_info()[0],sys.exc_info()[1])
        else:
            if verbose: print('copying dir',pathFrom,'to',pathTo)
            try:
                os.mkdir(pathTo)
                below = copyTree(pathFrom,pathTo)
                fcount += below[0]
                dcount += below[1]
                dcount += 1
            except:
                print('Error creating',pathTo,'--skipped')
                print(sys.exc_info()[0],sys.exc_info()[1])
            
    return (fcount,dcount)

def getargs():
    """
    Get and verify directory name args, return default None on errors
    """
    try:
        dirFrom,dirTo = sys.argv[1:]
    except:
        print('Usage error: cpall.py dirFrom dirTo')
    else:
        if not os.path.isdir(dirFrom):
            print('Error: dirFrom is not a directory')
        elif not os.path.exists(dirTo):
            os.mkdir(dirTo)
            print('Note: dirTo was created')
            return(dirFrom,dirTo)
        else:
            print('Warning: dirTo already exists')
            if hasattr(os.path, 'samfile'):
                same = os.path.samefile(dirFrom, dirTo)
            else:
                same = os.path.abspath(dirFrom) == os.path.abspath(dirTo)
                
            if same:
                print('Error: dirFrom same as dirTo')
            else:
                return (dirFrom,dirTo)
            
            
if __name__ == '__main__':
    import time
    dirstuple = getargs()
    if dirstuple:
        print('Copying...')
        start = time.clock()
        fcount,dcount = copyTree(*dirstuple)
        print('Copied', fcount, 'files,', dcount, 'directories', end=' ')
        print('in', time.clock() - start, 'seconds')       
