# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:38:14 2021

@author: NGWASHIRONALD
"""
import os
import tkinter
from tkinter import Button, Entry, Tk, filedialog
from typing import Text 
import PyPDF2
from matplotlib.pyplot import text
from pandas.io.sql import pandasSQL_builder
import readDatFile
import sqlite3
import pandas as pd
from tkinter import messagebox
from tkinter import ttk




#=====================================================================================================================================================================

#Conversion factors to be used for Unitsand conversion window

unit_dict = {
    "cm" : 0.01,
    "m" : 1.0,
    "km": 1000.0,
    "feet": 0.3048,
    "miles": 1609.344,
    "inches": 0.0254,
    "grams" : 1.0,
    "kg" : 1000.0,
    "quintals": 100000.0,
    "tonnes" : 1000000.0,
    "pounds" : 453.592,
    "sq. m" : 1.0,
    "sq. km": 1000000.0,
    "are" : 100.0,
    "hectare" : 10000.0,
    "acre": 4046.856,
    "sq. mile" : 2590000.0,
    "sq. foot" : 0.0929,
    "cu. cm" : 0.001,
    "Litre" : 1.0,
    "ml" : 0.001,
    "gallon": 3.785
}

lengths = ["cm", "m", "km", "feet", "miles", "inches",]
weights = ["kg", "grams", "quintals", "tonnes", "pounds",]
temps = ["Celsius", "Fahrenheit"]
areas = ["sq. m", "sq. km", "are", "hectare", "acre", "sq. mile", "sq. foot"]
volumes = ["cu. cm", "Litre", "ml", "gallon"]

# Options for drop-down menu
OPTIONS = ["select units",
            "cm",
            "m",
            "km",
            "feet",
            "miles",
            "inches",
            "kg",
            "grams",
            "quintals",
            "tonnes",
            "pounds",
            "Celsius",
            "Fahrenheit",
            "sq. m",
            "sq. km",
            "are",
            "hectare",
            "acre",
            "sq. mile",
            "sq. foot",
            "cu. cm",
            "Litre",
            "ml",
            "gallon"]

#=====================================================================================================================================================================
#Menu functions HERE

# Fuction to load data file into the program 



#===================================================================================================================

def donothing():
    x = 0

def openfile():
    filedialog.askopenfile(initialdir = "F:\PVT Project\PVT_Ronald_2021\PVTfree-master", title = 
                                       "Select a File", filetypes=(("Text Files",".txt"),("All Files", "*.*")))
    
#Open files for the help menu
#Installing PVTfree
def HowInstall():
    os.system("Install_PVTfree.pdf")
    
#User Guide
def UserGuide():
    os.system("PVTfree_v1.pdf")
    
#About page
def AboutPVT():
    os.system("README.txt")

def openfolder():
    filedialog.askdirectory(initialdir = "F:\PVT Project\PVT_Ronald_2021\PVTfree-master", title = 
                                       "Select a Project")

def saveasfile():
    filedialog.asksaveasfile(initialdir = "F:\PVT Project\PVT_Ronald_2021\PVTfree-master", title = 
                                       "Save As...")
    
#=========================================================================================================================================================================
#Tkinter GUI starts here

root = tkinter.Tk()
root.title("PVTFree")
root.minsize(width=1080, height=1080)
root.config(padx = 20, pady=20)

menubar = tkinter.Menu(root)

#file options 

filemenu = tkinter.Menu(menubar, tearoff = 0)
filemenu.add_command(label = "New File", command = donothing)
filemenu.add_command(label = "Open File...", command = openfile)
filemenu.add_command(label = "New Project", command = donothing)
filemenu.add_command(label = "Open Project...", command = openfolder)
filemenu.add_command(label = "Import", command = donothing)
filemenu.add_command(label = "Export", command = donothing)
filemenu.add_command(label = "Save", command = saveasfile)
filemenu.add_command(label = "Save As...", command = saveasfile)
filemenu.add_command(label = "Delete Project...", command = donothing)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.destroy)
menubar.add_cascade(label="File", menu = filemenu)

#========================================================================================
#writing the text from an entry into a text file



#========================================================================================

#Option menu
def open_menu():
  
  top = tkinter.Toplevel()
  top.title("Options")
  #top.minsize(width=500, height=500)
  #top.config(padx = 20, pady=20)
  
  #Select the equation of state, either Peng-Robinson or Soave-Relich-Kwong

  EOSframe = tkinter.LabelFrame(top, text = "Equation of State", padx = 20, pady = 20)
  EOSframe.grid(column = 0, row = 0)
 
  #Select either PR or SRK
  EOS_menu = tkinter.Label(EOSframe, text = "Equation of State (EOS)")
  EOS_menu.grid(row = 2, column =0)

  #Creating EOS options
  def comboclick(event):
    EOSOptionsSelected = myCombo.get()
    if EOSOptionsSelected == "PR":
      print("PR") 
    else:
      print("SRK")

  EOSOptions = ["PR", "SRK", ]
  myCombo = ttk.Combobox(EOSframe, value=EOSOptions)
  myCombo.current(0)
  myCombo.bind("<<ComboboxSelected>>", comboclick)
  myCombo.grid(row=2, column=1)

  #Number of pseudo-components 
  CompSplit = tkinter.Label(EOSframe, text="Split")
  CompEntry = tkinter.Entry(EOSframe)
  CompSplit.grid(column=0, row=3)
  CompEntry.grid(column=1, row=3)
 
#User Information

  #Get user information and save in a file called UserInformation 
  def SaveUserInfo():
        SaveCompanyName = CompanyNameEntry.get()
        SaveFieldName = FieldNameEntry.get()
        SaveLocationName = LocationNameEntry.get()
        SavePlatformName = PlatformNameEntry.get()
        SaveAnalystName = AnalystNameEntry.get()
        #SaveComment  = CommentText.get()

        LoadInfoFile = open("InfoFile.txt", "a")
        LoadInfoFile.write("\n")
        LoadInfoFile.write(SaveCompanyName)
        LoadInfoFile.write("\n")
        LoadInfoFile.write(SaveFieldName)
        LoadInfoFile.write("\n")
        LoadInfoFile.write(SaveLocationName)
        LoadInfoFile.write("\n")
        LoadInfoFile.write(SavePlatformName)
        LoadInfoFile.write("\n")
        LoadInfoFile.write(SaveAnalystName)
        LoadInfoFile.write("\n")
        #LoadInfoFile.write(SaveComment)
        LoadInfoFile.write("\n")

      
  
  UserInfoframe = tkinter.LabelFrame(top, text = "User Information", padx = 10, pady = 10)
  UserInfoframe.grid(column = 1, row = 0)
  CompanyName = tkinter.Label(UserInfoframe, text = "Company Name")
  CompanyName.grid(column = 0, row = 1)
  CompanyNameEntry = tkinter.Entry(UserInfoframe, width = 30)
  CompanyNameEntry.grid(column = 1, row = 1)
  
  FieldName = tkinter.Label(UserInfoframe, text = "Field")
  FieldName.grid(column = 0, row = 2)
  FieldNameEntry = tkinter.Entry(UserInfoframe, width = 30)
  FieldNameEntry.grid(column = 1, row = 2)
  
  LocationName = tkinter.Label(UserInfoframe, text = "Location")
  LocationName.grid(column = 0, row = 3)
  LocationNameEntry = tkinter.Entry(UserInfoframe, width = 30)
  LocationNameEntry.grid(column = 1, row = 3)
  
  PlatformName = tkinter.Label(UserInfoframe, text = "Platform")
  PlatformName.grid(column = 0, row = 4)
  PlatformNameEntry = tkinter.Entry(UserInfoframe, width = 30)
  PlatformNameEntry.grid(column = 1, row = 4)
  
  AnalystName = tkinter.Label(UserInfoframe, text = "Analyst")
  AnalystName.grid(column = 0, row = 5)
  AnalystNameEntry = tkinter.Entry(UserInfoframe, width = 30)
  AnalystNameEntry.grid(column = 1, row = 5)
  
#Comments 
  CommentText = tkinter.Text(top, height=15, width=60 )
    #Puts cursor in textbox
  CommentText.focus()
    #Adds some text to begin with
  CommentText.insert(tkinter.END, "Insert any comments...")
    #Gets current value in textbox at line , 
    #character 0
  print(CommentText.get("1.0", tkinter.END))
  CommentText.grid(column= 0, row = 1, columnspan = 30)
  
  UserGuideframe = tkinter.LabelFrame(top, text = "User Guide", width = 20, height = 100, padx = 20, pady =20)
  UserGuideframe.grid(column = 3, row = 0)
  title = tkinter.Label(UserGuideframe, text = "User Guide")
  title.grid(column = 0, row = 1)

  #Creating buttom buttons 
  def action():
        print("Do Something")   #Calls action() when pressed 
        
  OkButton = tkinter.Button(top, text="Ok", command=NewSample)  #fix this later 
  OkButton.config(padx = 5, pady = 5)
  OkButton.grid(column =0, row =4, pady =10)
  
  ApplyButton = tkinter.Button(top, text="Apply", command=donothing)
  ApplyButton.config(padx = 5, pady = 5)
  ApplyButton.grid(column =1, row =4, pady= 10)
  
  CancelButton = tkinter.Button(top, text="Cancel", command=top.destroy)
  CancelButton.config(padx = 5, pady = 5)
  CancelButton.grid(column =2, row = 4, pady = 10)  
 

# Function for the Unit conversion window 
#======================================================================================================================
def UnitConv():
  #Units for CGR
  # Creating CGR entry 
  UnitConvWindow = tkinter.Toplevel()
  UnitConvWindow.title("Unit Converter")
  def ok():
    inp = float(inputentry.get())
    inp_unit = inputopt.get()
    out_unit = outputopt.get()

    cons = [inp_unit in lengths and out_unit in lengths,
    inp_unit in weights and out_unit in weights,
    inp_unit in temps and out_unit in temps,
    inp_unit in areas and out_unit in areas,
    inp_unit in volumes and out_unit in volumes]

    if any(cons): # If both the units are of same type, do the conversion
        if inp_unit == "Celsius" and out_unit == "Fahrenheit":
            outputentry.delete(0, tkinter.END)
            outputentry.insert(0, (inp * 1.8) + 32)
        elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
            outputentry.delete(0, tkinter.END)
            outputentry.insert(0, (inp - 32) * (5/9))
        else:
            outputentry.delete(0, tkinter.END)
            outputentry.insert(0, round(inp * unit_dict[inp_unit]/unit_dict[out_unit], 5))

    else: # Display error if units are of different types
        outputentry.delete(0, tkinter.END)
        outputentry.insert(0, "ERROR")

  inputopt = tkinter.StringVar()
  inputopt.set(OPTIONS[0])

  outputopt = tkinter.StringVar()
  outputopt.set(OPTIONS[0])

  # Widgets
  inputlabel = tkinter.Label(UnitConvWindow, text = "Input")
  inputlabel.grid(row = 0, column = 0, pady = 20)

  inputentry = tkinter.Entry(UnitConvWindow, justify = "center", font = "bold")
  inputentry.grid(row = 1, column = 0, padx = 35, ipady = 5)

  inputmenu = tkinter.OptionMenu(UnitConvWindow, inputopt, *OPTIONS)
  inputmenu.grid(row = 1, column = 1)
  inputmenu.config(font = "Arial 10")

  outputlabel = tkinter.Label(UnitConvWindow, text = "Output")
  outputlabel.grid(row = 2, column = 0, pady = 20)

  outputentry = tkinter.Entry(UnitConvWindow, justify = "center", font = "bold")
  outputentry.grid(row = 3, column = 0, padx = 35, ipady = 5)

  outputmenu = tkinter.OptionMenu(UnitConvWindow, outputopt, *OPTIONS)
  outputmenu.grid(row = 3, column = 1)
  outputmenu.config(font = "Arial 10")

  okbtn = tkinter.Button(UnitConvWindow, text = "OK", command = ok, padx = 80, pady = 2)
  okbtn.grid(row = 4, column = 0, columnspan = 2, pady = 50)

#Creating options menu 
optionmenu = tkinter.Menu(menubar, tearoff = 0)
optionmenu.add_command(label = "Options...", command = open_menu)
optionmenu.add_command(label = "Units", command = UnitConv)
menubar.add_cascade(label="Options", menu=optionmenu)
#============================================================================================================================
#Adding a new Sample function
    


#=========================================================================================================================
#Developing database to contain pseudo-components 
def ButtonAction():
    #creating a basic secondary window with width and height of 500
  NewSampleFrame = tkinter.Toplevel()
  NewSampleFrame.title("New Sample")
  #create a database or connect to one 
  conn = sqlite3.connect("pseudocomponents.db")
  #create a cursor 
  c = conn.cursor()

  #create a table 
  #c.execute("""CREATE TABLE addresses (
  #samples text,
  #molecular_weight real,
  #specific_gravity real,
  #alpha real,
  #nitrogen real,
  #carbondioxide real,
  #hydrogen_sulphide real,
  #carbon_one real,
  #carbon_two real,
  #carbon_three real,
  #i_carbon_four real,
  #n_carbon_four real,
  #i_carbon_five real,
  #n_carbon_five real,
  #carbon_six real,
  #carbon_seven_plus real
 # )""")

  #Create submit button for sqlite database 
  def submit():

    #create a database or connect to one 
    conn = sqlite3.connect("pseudocomponents.db")

     #create a cursor 
    c = conn.cursor()

    #Insert into table 
    c.execute("INSERT INTO addresses VALUES (:samples, :molecular_weight,:specific_gravity,:alpha,:nitrogen,:carbondioxide,:hydrogen_sulphide,:carbon_one,:carbon_two,:carbon_three,:i_carbon_four,:n_carbon_four,:i_carbon_five,:n_carbon_five,:carbon_six,:carbon_seven_plus)",
              {
                  'samples':samples.get(),
                  'molecular_weight':molecular_weight.get(),
                  'specific_gravity':specific_gravity.get(),
                  'alpha':alpha.get(),
                  'nitrogen':nitrogen.get(),
                  'carbondioxide':carbondioxide.get(),
                  'hydrogen_sulphide':hydrogen_sulphide.get(),
                  'carbon_one':carbon_one.get(),
                  'carbon_two':carbon_two.get(),
                  'carbon_three':carbon_three.get(),
                  'i_carbon_four':i_carbon_four.get(),
                  'n_carbon_four':n_carbon_four.get(),
                  'i_carbon_five':i_carbon_five.get(),
                  'n_carbon_five':n_carbon_five.get(),
                  'carbon_six':carbon_six.get(),
                  'carbon_seven_plus':carbon_seven_plus.get()
              })

    #commit changes
    conn.commit()

    #close connection 
    conn.close()

    #clear the textboxes 
    samples.delete(0, tkinter.END)
    molecular_weight.delete(0,tkinter.END) 
    specific_gravity.delete(0, tkinter.END)
    alpha.delete(0,tkinter.END)
    nitrogen.delete(0,tkinter.END)
    carbondioxide.delete(0,tkinter.END)
    hydrogen_sulphide.delete(0, tkinter.END)
    carbon_one.delete(0,tkinter.END)
    carbon_two.delete(0, tkinter.END)
    carbon_three.delete(0, tkinter.END)
    i_carbon_four.delete(0, tkinter.END)
    n_carbon_four.delete(0,tkinter.END)
    i_carbon_five.delete(0, tkinter.END)
    n_carbon_five.delete(0, tkinter.END)
    carbon_six.delete(0, tkinter.END)
    carbon_seven_plus.delete(0,tkinter.END)

  #create textboxes  
  samples = tkinter.Entry(NewSampleFrame,width=30)
  samples.grid(row=0, column=1, padx=20)

  molecular_weight = tkinter.Entry(NewSampleFrame,width=30)
  molecular_weight.grid(row=1, column=1)

  specific_gravity = tkinter.Entry(NewSampleFrame,width=30)
  specific_gravity.grid(row=2, column=1, padx=20)

  alpha = tkinter.Entry(NewSampleFrame,width=30)
  alpha.grid(row=3, column=1, padx=20)

  nitrogen = tkinter.Entry(NewSampleFrame,width=30)
  nitrogen.grid(row=4, column=1, padx=20)

  carbondioxide = tkinter.Entry(NewSampleFrame,width=30)
  carbondioxide.grid(row=5, column=1, padx=20)

  hydrogen_sulphide = tkinter.Entry(NewSampleFrame,width=30)
  hydrogen_sulphide.grid(row=6, column=1, padx=20)

  carbon_one = tkinter.Entry(NewSampleFrame,width=30)
  carbon_one.grid(row=7, column=1, padx=20)

  carbon_two = tkinter.Entry(NewSampleFrame,width=30)
  carbon_two.grid(row=8, column=1, padx=20)

  carbon_three = tkinter.Entry(NewSampleFrame,width=30)
  carbon_three.grid(row=9, column=1, padx=20)

  i_carbon_four = tkinter.Entry(NewSampleFrame,width=30)
  i_carbon_four.grid(row=10, column=1, padx=20)

  n_carbon_four = tkinter.Entry(NewSampleFrame,width=30)
  n_carbon_four.grid(row=11, column=1, padx=20)

  i_carbon_five = tkinter.Entry(NewSampleFrame,width=30)
  i_carbon_five.grid(row=12, column=1, padx=20)

  n_carbon_five = tkinter.Entry(NewSampleFrame,width=30)
  n_carbon_five.grid(row=13, column=1, padx=20)

  carbon_six = tkinter.Entry(NewSampleFrame,width=30)
  carbon_six.grid(row=14, column=1, padx=20)

  carbon_seven_plus = tkinter.Entry(NewSampleFrame,width=30)
  carbon_seven_plus.grid(row=15, column=1, padx=20)

  #create text box labels 
  samples_label = tkinter.Label(NewSampleFrame, text="SAMPLES")
  samples_label.grid(row=0, column=0)

  molecular_weight_label = tkinter.Label(NewSampleFrame, text="MOLECULAR WEIGHT")
  molecular_weight_label.grid(row=1, column=0)

  specific_gravity_label = tkinter.Label(NewSampleFrame, text="SPECIFIC GRAVITY")
  specific_gravity_label.grid(row=2, column=0)

  alpha_label = tkinter.Label(NewSampleFrame, text="ALPHA")
  alpha_label.grid(row=3, column=0)

  nitrogen_label = tkinter.Label(NewSampleFrame, text="N2")
  nitrogen_label.grid(row=4, column=0)

  carbondioxide_label = tkinter.Label(NewSampleFrame, text="CO2")
  carbondioxide_label.grid(row=5, column=0)

  hydrogen_sulphide_label = tkinter.Label(NewSampleFrame, text="H2S")
  hydrogen_sulphide_label.grid(row=6, column=0)

  carbon_one_label = tkinter.Label(NewSampleFrame, text="C1")
  carbon_one_label.grid(row=7, column=0)

  carbon_two_label = tkinter.Label(NewSampleFrame, text="C2")
  carbon_two_label.grid(row=8, column=0)

  carbon_three_label = tkinter.Label(NewSampleFrame, text="C3")
  carbon_three_label.grid(row=9, column=0)

  i_carbon_four_label = tkinter.Label(NewSampleFrame, text="iC4")
  i_carbon_four_label.grid(row=10, column=0)

  n_carbon_four_label = tkinter.Label(NewSampleFrame, text="nC4")
  n_carbon_four_label.grid(row=11, column=0)

  i_carbon_five_label = tkinter.Label(NewSampleFrame, text="iC5")
  i_carbon_five_label.grid(row=12, column=0)

  n_carbon_five_label = tkinter.Label(NewSampleFrame, text="nC5")
  n_carbon_five_label.grid(row=13, column=0)

  carbon_six_label = tkinter.Label(NewSampleFrame, text="C6")
  carbon_six_label.grid(row=14, column=0)

  carbon_seven_plus_label = tkinter.Label(NewSampleFrame, text="C7+")
  carbon_seven_plus_label.grid(row=15, column=0)


  #create submit button
  submit_btn = tkinter.Button(NewSampleFrame, text="Create Sample", command=submit)
  submit_btn.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

  submit_btn = tkinter.Button(NewSampleFrame, text="Done", command=NewExperimentWindow)
  submit_btn.grid(row=17, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

  submit_btn = tkinter.Button(NewSampleFrame, text="Cancel", command=NewSampleFrame.destroy)
  submit_btn.grid(row=18, column=0, columnspan=2, pady=10, padx=10, ipadx=120)



  #commit changes
  conn.commit()

  #close connection 
  conn.close()
        
  #Creating button 
  #Button action

def NewSample():
  NewSampleFrame2 = tkinter.Toplevel()
  NewSampleFrame2.title("New Sample")   
  Insert_Sample_name = tkinter.Label(NewSampleFrame2, text="Enter the name (short) of the new sample")
  Insert_Sample_name.grid(row=0, column=0)
  Insert_Sample_name_entry = tkinter.Entry(NewSampleFrame2)
  Insert_Sample_name_entry.grid(row=1, column=0)  
  B1 = tkinter.Button(NewSampleFrame2, text = "Ok", command = ButtonAction)
  B2 = tkinter.Button(NewSampleFrame2, text = "Cancel", command = NewSampleFrame2.destroy)
  B1.grid(row = 0, column = 1, padx = 5, pady = 5, ipadx=30)
  B2.grid(row = 1, column = 1, padx = 5, pady = 5, ipadx=20)
 
#Sample option
samplemenu = tkinter.Menu(menubar, tearoff = 0)
samplemenu.add_command(label = "Add sample...", command = NewSample)
samplemenu.add_command(label = "Modify Sample", command = ButtonAction)
menubar.add_cascade(label="Samples", menu=samplemenu)

#===========================================================================================================================================
#Create experiment routine 
#write function to write experiment to text file

def SaveFileWindow():
    from PVTfree import PVTfree




#experiment option
def NewExperimentWindow():
  NewExpWindow = tkinter.Toplevel()
  NewExpWindow.title("New Experiment")
  
  
  #Load experiment data
  #Experiment options supported include 
  #CCE --- Constant Compostion Expansion
  #CVD --- Constant Volume Depletion
  #DLE --- Differential Liberation Experiment 
  #SEP --- Separator Test 
  #PSAT -- Saturation Pressure Calculation
  #FLASH - Two-Phase Flash Calculations 
  #SWELL - Swelling Test
  #GRAD -- Compostional Grading (Compostion Versus Depth)



  #=====================================================================================================================
  #View file imported
  def View_file_button():
    from tkinter import filedialog as fd 
    #Root window
    viewWindow = tkinter.Tk()
    viewWindow.title('Display a Text File')
    viewWindow.resizable(False, False)
    viewWindow.geometry('550x550')

    #Text editor 
    text = tkinter.Text(viewWindow, height = 12)
    text.grid(column=0, row=0, sticky='nsew')   

    def open_test_file():
        #file type 
      filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
      )
    #show the open file dialog 
      f = fd.askopenfile(filetypes = filetypes)
      #read the text file and show its content on the text 
      text.insert('1.0', f.readlines())

    #open file button 
    open_button = ttk.Button(
    viewWindow,
    text = 'Open as File',
    command=open_test_file
    )

    open_button.grid(column=0, row=1, sticky='w', padx=10,pady=10)
    viewWindow.mainloop()

  ViewLoadedFile = ttk.Button(NewExpWindow, text = 'View File', command=View_file_button)
  ViewLoadedFile.grid(row=2, column=0)

  #Add Experiment 
  #Load button ---- (drop down or checkbox)
  #have the options to select one or more 
  #then run

  def SelectExperimentWindow():
    SelectExperimentWindowOpen = tkinter.Toplevel()
    SelectExperimentWindowOpen.title("Select Exeriment")

    #loads the files from the checkboxes 

    ExperimentCheckBoxCCE = tkinter.Button(SelectExperimentWindowOpen, text = "CCE", command = import_Exp_data) 

    ExperimentCheckBoxCVD = tkinter.Button(SelectExperimentWindowOpen, text = "CVD", command = import_Exp_data) 

    ExperimentCheckBoxDLE = tkinter.Button(SelectExperimentWindowOpen, text = "DLE", command = import_Exp_data) 

    ExperimentCheckBoxSEP = tkinter.Button(SelectExperimentWindowOpen, text = "SEP", command = import_Exp_data) 

    ExperimentCheckBoxPSAT = tkinter.Button(SelectExperimentWindowOpen, text = "PSAT", command = import_Exp_data) 

    ExperimentCheckBoxFLASH = tkinter.Button(SelectExperimentWindowOpen, text = "FLASH", command = import_Exp_data) 

    ExperimentCheckBoxSWELL = tkinter.Button(SelectExperimentWindowOpen, text = "SWELL", command = import_Exp_data) 

    ExperimentCheckBoxGRAD = tkinter.Button(SelectExperimentWindowOpen, text = "GRAD", command = import_Exp_data) 

    ExperimentCheckBoxCCE.grid(row=0, column=0,padx = 5, pady = 5, ipadx=20)
    ExperimentCheckBoxCVD.grid(row=0, column=1,padx = 5, pady = 5, ipadx=20)
    ExperimentCheckBoxDLE.grid(row=0, column=2,padx = 5, pady = 5, ipadx=20)
    ExperimentCheckBoxSEP.grid(row=0, column=3,padx = 5, pady = 5, ipadx=20)
    ExperimentCheckBoxPSAT.grid(row=1, column=0,padx = 5, pady = 5, ipadx=15)
    ExperimentCheckBoxFLASH.grid(row=1, column=1,padx = 5, pady = 5, ipadx=15)
    ExperimentCheckBoxSWELL.grid(row=1, column=2,padx = 5, pady = 5, ipadx=15)
    ExperimentCheckBoxGRAD.grid(row=1, column=3,padx = 5, pady = 5, ipadx=15)

    Ok_button = tkinter.Button(SelectExperimentWindowOpen, text = "Ok", command = SelectExperimentWindowOpen.destroy)    
    cancel_button = tkinter.Button(SelectExperimentWindowOpen, text = "Cancel", command = SelectExperimentWindowOpen.destroy)
    Ok_button.grid(row = 2, column = 0, padx = 5, pady = 5, ipadx=20)
    cancel_button.grid(row = 2, column = 1, padx = 5, pady = 5, ipadx=20)


  SelectExperimentBut = ttk.Button(NewExpWindow, text = 'Select Experiment', command=SelectExperimentWindow)
  SelectExperimentBut.grid(row=2, column=1)

  #===========================================================================================================================================

#import experiment data with the right format as a CSV file
  def import_Exp_data():
    filename = filedialog.askopenfile(initialdir = "F:\PVT Project\PVT_Ronald_2021\PVTfree-master", title = 
                                       "Import Experiment Data", filetypes=(("Text Files",".txt"),("All Files","*.*")))


   
  fluid_type = tkinter.Label(NewExpWindow, text="Fluid Type")
  fluid_type.grid(row=3, column=0)

  #Creating fluid options  
  fluid_type_Options = ["BLACK OIL", "VOLATILE OIL", "CONDENSATE", "WET GAS", "DRY GAS" ]
  default_value = tkinter.StringVar()
  default_value.set('Select')
  fluid_type_option_menu = tkinter.OptionMenu(NewExpWindow, default_value, *fluid_type_Options, command=donothing)
  fluid_type_option_menu.grid(row=3, column=1,padx = 5, pady = 5, ipadx=20)

  #Reservoir Temperature
  reservoir_temp = tkinter.Label(NewExpWindow, text="Reservoir Temperature (degF)")
  reservoir_temp.grid(row=4, column=0)
  reservoir_temp_entry = tkinter.Entry(NewExpWindow)
  reservoir_temp_entry.grid(row=4, column=1, columnspan=2,padx = 5, pady = 5, ipadx=40)

  regression_label = tkinter.Label(NewExpWindow, text="Experiment Type Data")
  regression_label.grid(row=5, column=0)


  Ok_button = tkinter.Button(NewExpWindow, text = "Ok", command = generate_file)
  run_regression_button = tkinter.Button(NewExpWindow, text = "Run", command=SaveFileWindow)
  cancel_button = tkinter.Button(NewExpWindow, text = "Cancel", command = NewExpWindow.destroy)
  Ok_button.grid(row = 6, column = 0, padx = 5, pady = 5, ipadx=20)
  run_regression_button.grid(row = 6, column = 1, padx = 5, pady = 5, ipadx=20)
  cancel_button.grid(row = 6, column = 2, padx = 5, pady = 5, ipadx=20)

#End of experiment option
#============================================================================================================================================

experimentmenu = tkinter.Menu(menubar, tearoff = 0)
experimentmenu.add_command(label = "Add Experiment...", command = NewExperimentWindow)
experimentmenu.add_command(label = "Modify Experiment", command = NewExperimentWindow)
menubar.add_cascade(label="Experiments", menu=experimentmenu)

#view option
viewmenu = tkinter.Menu(menubar, tearoff = 0)
viewmenu.add_command(label = "Plots", command = donothing)
viewmenu.add_command(label = "Report", command = donothing)
menubar.add_cascade(label="View", menu=viewmenu)

#window option
windowmenu = tkinter.Menu(menubar, tearoff = 0)
windowmenu.add_command(label = "Cascade", command = donothing)
windowmenu.add_command(label = "Tile", command = donothing)
menubar.add_cascade(label="Window", menu=windowmenu)

#Help option  #creating window for reporting bugs 
def ReportBugs():
  #creating a basic secondary window with width and height of 500
  bug = tkinter.Toplevel()
  bug.title("Issue Reporter")
 
  Paragraph1 = tkinter.Label(bug, text = """Before reporting any problems, please ensure you have read the manual carefully and understood the software.
  This will help in your problem. If not, fill the form below and we will solve your issue.""")
  Paragraph1.grid(row = 0, column = 0, columnspan = 30)
      
  Paragraph2 = tkinter.Label(bug, text = "Please fill the follwing information.")
  Paragraph2.grid(row =1, column =0, columnspan = 30, pady =5)
      
  Title = tkinter.Label(bug, text = "Title")
  Title.grid(row = 2, column =0, sticky = tkinter.W, pady = 7)
  TitleEntry = tkinter.Entry(bug, width = 85)
  TitleEntry.grid(row = 2, column = 1)
      
    
  #Creating a text widget 
  T = tkinter.Text(bug)
  Paragraph = """--------------Insert your complain here! --------------"""
  T.grid(row = 3, column = 0, columnspan = 30)
  T.insert(tkinter.END, Paragraph)
      
  #Creating button 
  B1 = tkinter.Button(bug, text = "Submit to GitHub")
  B2 = tkinter.Button(bug, text = "Close", command = bug.destroy)
  B1.grid(row = 4, column = 0, sticky = tkinter.W, padx = 5, pady = 5)
  B2.grid(row = 4, column = 1, sticky = tkinter.W, padx = 5, pady = 5)

helpmenu = tkinter.Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "Documentation", command = UserGuide)
helpmenu.add_command(label = "Report Bugs", command = ReportBugs)
helpmenu.add_command(label = "How to Install", command = HowInstall)
helpmenu.add_command(label = "About...", command = AboutPVT)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu = menubar)

#creating home frame 
#creating a frame 
frame = tkinter.LabelFrame(root, padx = 10, pady = 10)
frame.pack()
title = tkinter.Label(frame, text = "User guide")
title.grid(column = 0, row = 1,sticky=tkinter.N+tkinter.E+tkinter.W)

#======================================================================================================================================

def generate_file():
    with open("NewPVTfile.dat","a") as f:
      f.write("\n")
      f.write("--========================================================\n")
      f.write("--EOS PVT Program\n")
      f.write("--Code by Steve Furnival, GUI by Ngwashi Ronald Afungchwi and Prof. David O. Ogbe\n\n")

      f.write("--========================================================\n")
      f.write("--Fluid Initialisation\n")
      f.write("--========================================================\n \n")

      f.write("INIT \n \n")
      #load_new_file.write("ENV     1 \n")
      #load_new_file.write("TSAT    1 \n")
      #load_new_file.write("ENDDEB \n \n")

      EOS_insert = input("Enter equation of State (PR or SRK): ")
      

      f.write("EOS   " + EOS_insert)
      #if EOS == PR or SRK write them here in file 
      f.write("\n\n")

      split_number = input("Enter number of split: ")

      f.write("--Number of pseudocomponents to be split from C7+\n\n")
      f.write("SPLIT   " + split_number)
      #collect the value from split input and write it here

      f.write("\n \n")
      f.write("--Sample Definitions \n\n")
      #load samples data here 
      Load_samples = open("Sample_data.txt", "r")
      for lines0 in Load_samples:
          f.write(lines0)

      f.write("\n\n")
      f.write("ENDINIT \n")
      
      #load experiment data 
      f.write("--==============================================================\n")
      f.write("--Experiments \n")
      f.write("--==============================================================\n\n")
      f.write("EXP \n\n")

      Load_CCE = open("CCE_data.txt","r")
      Load_DLE = open("DLE_data.txt","r")
      Load_DLE_2 = open("DLE_data2.txt","r")
      Load_SEP = open("SEP_data.txt","r")
      Load_SEP_2 = open("SEP_data2.txt","r")


      for lines in Load_CCE:
          f.write(lines)
      f.write(" \n")
      for lines3 in Load_DLE:
          f.write(lines3)
      f.write(" \n")
      # for lines4 in Load_SEP:
      #     f.write(lines4)
      #     f.write(" \n")
      # for lines4 in Load_SEP_2:
      #     f.write(lines4)
      #     f.write(" \n")
      for lines2 in Load_DLE_2: 
          f.write(lines2)
      f.write(" \n")    

      f.write("\n\n \n")
      f.write("ENDEXP \n\n")

      f.write("--==============================================================\n")
      f.write("--STOP \n")
      f.write("--==============================================================\n\n")
      f.write("STOP \n\n")  
     

root.mainloop()

'''
Add Experiment 
Load button ---- (drop down or checkbox)
have the options to select one or more 
then run

call the plot to the screen (view plots)
view more or one plot (check box)
run correlations for detailed fluid characterization
'''