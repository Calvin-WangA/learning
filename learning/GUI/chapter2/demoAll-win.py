'''
Created on 2016年3月4日

@author: CasparWang
'''
"""
4 demo classes in independent top-level windows;
not processes: when one is quit all others go away, because all windows run in
the same process here; make Tk() first here, else we get blank default window
"""
from tkinter import *
demoModules = ['demoDlg','demoRadio','demoCheck','demoScale']

def makePopups(modnames):
    demoObjects = []
    for modname in modnames:
        module = __import__(modname)             # import module by string name
        window = Toplevel()                      # make a new window
        demo = module.Demo(window)               # parent is a new window
        window.title(module.__name__)
        demoOjbects.append(demo)
        
    return demoObjects
def allstates(demoObjects):
    for obj in demoOjbects:
        if hasattr(obj, 'report'):
            print(obj.__module__,end='')
            obj.report()
            
root = Tk()
root.title('Popups')
demos = makePopups(demoModules)
Label(root,text='Multiple Toplevel window demo', bg=white).pack()
Button(root,text='States',command=(lambda: allstates(demos))).pack(fill=X)
root.mainloop()