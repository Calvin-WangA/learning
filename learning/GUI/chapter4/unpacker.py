#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月14日

@author: CasparWang
'''
import sys
from learning.GUI.chapter4.packer import maker
mlen = len(maker)

def unpack(ifile, prefix='new-'):
    for line in open(ifile):
        if line[:mlen] != maker:
            output.write(line)
        else:
            name = prefix + line[mlen:-1]
            print('creating:', name)
            output = open(name, 'w')
            
if __name__ == '__main__':
    unpack(sys.argv[1])
    