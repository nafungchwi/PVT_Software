import tkinter as tk


#we want to create an entry widget to hold a value
#and do something with it

def save():
      file_name = entry.get()
      with open(file_name + '.txt', 'w') as file_object:
        file_object.write(file_name)

if __name__ == '__main__':
      top = tk.Tk()
      entry_field_variable = tk.StringVar()
      entry = tk.Entry(top, textvariable = entry_field_variable)
      entry.pack()
      tk.Button(top, text = "save", command = save).pack()


top.mainloop()