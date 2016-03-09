#!usr/local/bin/local
#coding: utf-8
'''
Created on 2016年3月9日

@author: CasparWang
'''
"""
implement sum from 0 to n.
"""
def countSum(n):
    if n == 0:
        return n
    else:
        return (n + countSum(n - 1))
        
if __name__=='__main__':
    print(countSum(10))