#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月14日

@author: CasparWang
'''
"""
################################################################################
provide type-specific option sets for application
################################################################################
"""
from learning.GUI.chapter4.shellgui import *
from learning.GUI.chapter4.packdlg import runPackDialog  # dialogs for data entry
from learning.GUI.chapter4.unpkdlg import runUnpackDialog # they both run app classes

class TextPak1(ListMenuGui):
    def __init__(self):
        self.myMenu = [('Pack ', runPackDialog), # simple functions
                       ('Unpack', runUnpackDialog), # use same width here
                       ('Mtool ', self.notdone)] # method from guimixin
        ListMenuGui.__init__(self)
        
    def forToolBar(self, label):
        return label in {'Pack ', 'Unpack'}
    
class TextPak2(DictMenuGui):
    def __init__(self):
        self.myMenu = {'Pack ': runPackDialog, # or use input here...
                       'Unpack': runUnpackDialog, # instead of in dialogs
                       'Mtool ': self.notdone}
        DictMenuGui.__init__(self)
        
if __name__ == '__main__':
    from sys import argv
    if len(argv) > 1 and argv[1] == 'list':
        print('list test')
        TextPak1().mainloop()
    else:
        print('dict test')
        TextPak2().mainloop()
        
