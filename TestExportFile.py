''' #open the file and read the contents 
#f =open("SampleFile.txt", "r")
import readDataFile
import numpy as np

filename = open('GASandOIL.txt')
readcontent = filename.read()
print(readcontent)

def ReadFile():
    readDataFile()
 '''

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("My First GUI Plot")

def graph():
    house_prices = np.random.normal(200000, 25000,5000)
    plt.hist(house_prices, 50)
    plt.show()
my_button = Button(root, text = "Plot", command=graph)
my_button.pack()
root.mainloop()