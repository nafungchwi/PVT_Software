from tkinter import *
import numpy as np
import math 

root = Tk()
#This program calculate the PVT properties of Oil, Water, and gas 

# OIL CORRELATIONS 
# 1. Determine STOCK TANK OIL GRAVITY (Gamma_API) 
def gammaCalc():
    pass

Gamma_Label = Label(root, text="Specific gravity")
Gamma_Entry = Entry()

Gamma_Label.grid(row=0, column=0)
Gamma_Entry.grid(row=0, column=1)

Button_calc = Button(root, text="Calculate", command=gammaCalc)



root.mainloop()