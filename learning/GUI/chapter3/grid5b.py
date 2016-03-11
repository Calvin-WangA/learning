#!usr/local/bin/python
#coding: utf-8
'''
Created on 2016年3月10日

@author: CasparWang
'''
# recode as an embedable class
from tkinter import *
from tkinter.filedialog import askopenfilename
from learning.GUI.chapter2.quitter import Quitter

class SumGrid(Frame):
    def __init__(self, parent=None, numrow=5, numcol=5):
        Frame.__init(self,parent)
        self.numrow = numrow
        self.numcol = numcol
        self.makeWidgets(numrow, numcol)
        
    def makeWidgets(self, numrow, numcol):
        self.rows = []
        for i in range(numrow):
            cols = []
            for j in range(numcol):
                ent = Entry(self, relief=RIDGE)
                ent.grid(row=i + 1, column=j, sticky=NSEW)
                ent.insert(END, '%d.%d' %(i,j))
                cols.append(ent)
            self.rows.append(cols)
        sums = []
        for i in range(numcol):
            lab = Label(self, text='?', relief=SUNKEN)
            lab.grid(row=numrow + 1, column=i, sticky=NSEW)
            self.sums.append(lab)
            
        Button(self, text='sum', command=self.onSum).grid(row=0,column=0)
        Button(self, text='print', command=self.onPrint).grid(row=0, column=1)
        Button(self, text='clear', command=self.onClear).grid(row=0, column=2)
        Button(self, text='load', command=self.onLoad).grid(row=0,column=3)
        Quitter(self).grid(row=0,column=4)        #fails: Quitter(self).pack()
        
    def onPrint(self):
        for row in self.rows:
            for col in row:
                print(col.get(), end=' ')
            print()
        print()
        
    def onSum(self):
        tots = [0]*self.numcol
        for i in range(self.numcol):
            for j in range(self.numrow):
                tots[i] += eval(self.rows[j][i].get())
        for i in range(self.numcol):
            self.sums[i].config(text=str(tots[i]))
            
    def onClear(self):
        for row in self.rows:
            for col in row:
                col.delete('0', END)
                col.insert(END,'0.0')
        for sum in self.nums:
            sum.config(text='?')
            
    def onLoad(self):
        file = askopenfilename()
        if file:
            for row in self.rows:
                for col in row:
                    col.grid_forget()
            for sum in self.sums:
                sum.grid_forget()
            filelines = open(file,'r').readlines()
            self.numrow = len(filelines)
            self.numcol = len(filelines[0].split())
            self.makeWidgets(self.numrow, self.numcol)
            
            for (row, line) in enumerate(filelines):
                
                