from tkinter import *
root = Tk()

#Enter the EOS
labelEOS = Label(root, text="Enter EOS (PR or SRK)")
labelEOS.pack()
selectEOS = Entry(root)
selectEOS.pack()

root.mainloop()