import tkinter as tk
from tkinter import Text, ttk
from tkinter import filedialog as fd
import tkinter 

#Root window
root = tk.Tk()
root.title('Display a Text File')
root.resizable(False, False)
root.geometry('550x550')

EOSEntryLabel = tkinter.Label(root, text = "EOS (PR or SRK)")
EOSEntryLabel.grid(row=0, column=0)

EOSEntry = tkinter.Entry(root)
EOSEntry.grid(row=0, column=1)




def Submit():
    pass
    #getEntry = sampleEntry.get()
    #LoadFile = open("MySampleFile.txt", "a")
    #Newfile = LoadFile.write(getEntry)
    

SubmitButton = ttk.Button(root, text = "Submit", width=30, command=Submit)
SubmitButton.grid(row=1, column=0, columnspan=2)

root.mainloop()