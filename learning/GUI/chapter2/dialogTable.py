'''
Created on 2016年3月3日

@author: CasparWang
'''
# define a name: callback demos Table

from tkinter.filedialog import askopenfilename #get standard dialog
from tkinter.colorchooser import askcolor      # they live in Lib\tkinter
from tkinter.messagebox import askquestion,showerror
from tkinter.simpledialog import askfloat

demos = {
    'Open': askopenfilename,
    'Color': askcolor,
    'Query': lambda: askquestion('Warning','You typed "rm *"\nConfirm?'),
    'Error': lambda: showerror('Error!', "He's dead Jim"),
    'Input': lambda: askfloat('Entry','Enter credit card number')
    }
