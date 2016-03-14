#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月14日

@author: CasparWang
'''
# pack text files into a single file with separatorlines(simple archive)
import sys, glob 

maker = ":" * 20 + 'textpak=>'    # hopefully unique separator

def pack(ofile, ifiles):
    output =open(ofile, 'w')
    for name in ifiles:
        print('packing:', name)
        input = open(name, 'r').read()
        if input[-1] != '\n': input += '\n'
        output.write(maker + name + '\n')
        output.write(input)
        
if __name__ == '__main__':
    ifiles = []
    for patt in sys.argv[2:]:
        ifiles += glob.glob(patt)
    pack(sys.argv[1], ifiles)