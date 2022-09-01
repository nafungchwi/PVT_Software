from tkinter import *

#validates the input
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def convert_length(unit, event=None):

    if unit == 'm':

        val = mm_entry.get()             
        if (is_number(val)):
            mm = float(val)
            cm = mm / 10
            km = mm / 1000000     
            cm_entry.delete(0, END)
            km_entry.delete(0, END)
            cm_entry.insert(0, cm)
            km_entry.insert(0, km)

        else:
            cm_entry.delete(0, END)
            km_entry.delete(0, END)
            if (val == ''):
                cm_entry.insert(0, '')
                km_entry.insert(0, '')
            else:
                cm_entry.insert(0, 'NaN')
                km_entry.insert(0, 'NaN')



def get_option_value(unit):
    if unit == 'Length':
        length_frame.pack()

    if unit == 'Tempratur':
        print('Tempratur')

    if unit == 'Area':
       print('Area')

    if unit == 'Volume':
        print('Volume')

def convert_length(event, type):
    if type == 'm':
        print('do some stuff')

    if type == 'cm':
        print('do some stuff')

    if type == 'km':
        print('do some stuff')

window = Tk()

window.geometry('500x500')
window.resizable(0, 0)

t_frame = Frame(window, width=200, height=40)
b_frame = Frame(window, width=400, height=200)

t_frame.pack_propagate(0)
b_frame.pack_propagate(0)

t_frame.pack(padx=30, pady=10)
b_frame.pack(ipadx=20, ipady=20)

option_menu_label = Label(t_frame, text="Select Unit To Convert")
option_menu_label.pack()
options = ["Length", "Temprature", "Area", "Volume",]
default_value = StringVar()
default_value.set('Select Unit')
option_menu = OptionMenu(t_frame, default_value, *options, command=get_option_value)
option_menu.grid()

option_menu.pack()

# Length Converter

length_frame = Frame(b_frame, width=50, height=50)

mm_label = Label(length_frame, text="Millimeters").grid(row=0)
mm = IntVar()
mm_entry = Entry(length_frame, textvariable=mm)
mm_entry.bind("<Key>", lambda event: convert_length(event, 'm'))

cm_label = Label(length_frame, text="Centimeters").grid(row=1, column=0)
cm = IntVar()
cm_entry = Entry(length_frame, textvariable=cm)
cm_entry.bind("<Key>", lambda event: convert_length(event, 'cm'))

km_label = Label(length_frame, text="Kilometers").grid(row=2, column=0)
km = IntVar()
km_entry = Entry(length_frame, textvariable=km)
km_entry.bind("<Key>", lambda event: convert_length(event, 'k'))

# convert_length_button = Button(length_frame, text="Convert Length", command=convert_length)
mm_entry.grid(row=0, column=1)
cm_entry.grid(row=1, column=1)
km_entry.grid(row=2, column=1)
# convert_length_button.grid(columnspan=2)

# Temprature Converter

c_label = Label(b_frame, text="Celsius")
c = StringVar()
c_entry = Entry(b_frame, textvariable=c)

mm_label = Label(length_frame, text="Millimeters").grid(row=0)
mm_entry = Entry(length_frame)
mm_entry.bind("<KeyRelease>", lambda value : convert_length('m'))

window.mainloop()