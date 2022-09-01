import os
import sys
from tkinter import *
import tkinter
from tkinter import ttk

root = Tk()
Entry1 = Entry(root, width=50)
Entry1.pack()

def GetEntry1():
    new_file = open("newfile.txt", mode = "w", encoding="utf-8")
    getentry1 = Entry1.get()
    new_file.write(getentry1)
    new_file.close()
    
button1=Button(root, text="save Entry", command=GetEntry1)
button1.pack()

def SelectedEOSOptions(event):
    EOSOptionsSelected = default_value.get()
    if EOSOptionsSelected == "PR":
        print("PR") 
    else:
        print("SRK")

def comboclick(event):
    EOSOptionsSelected = myCombo.get()
    if EOSOptionsSelected == "PR":
        print("PR") 
    else:
        print("SRK")

EOSOptions = ["PR", "SRK", ]
default_value = StringVar()
default_value.set('Select EOS')
EOS_option_menu = OptionMenu(root, default_value, *EOSOptions, command=SelectedEOSOptions)
EOS_option_menu.pack()

myCombo = ttk.Combobox(root, value=EOSOptions)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()


root.mainloop()        

