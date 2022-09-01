import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter 

#Root window
root = tk.Tk()
root.title('Display a Text File')
root.resizable(False, False)
root.geometry('550x550')

sampleEntry = tkinter.Entry(root)
sampleEntry.pack()


root.mainloop()