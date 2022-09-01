# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 01:07:08 2021

@author: NGWASHIRONALD
"""

# importing required modules
from tkinter import *
import PyPDF2
from tkinter import filedialog

root = Tk()

myText = Text(root, height = 30, width = 60)
myText.pack(pady = 10)

#create menu
my_menu = Menu(root)
root.config(menu = my_menu)

#add some down menus 
file_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "File", menu=file_menu)
my_menu.add_command(label = "Open", command = open_pdf)
my_menu.add_command(label = "Clear", command = clear_text)
my_menu.add_separator()
my_menu.add_command(label = "Exit", command = root.quit)



root.mainloop()