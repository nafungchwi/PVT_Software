import tkinter
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd


root = tkinter.Tk()
root.title("PVTFree")
root.minsize(width=1080, height=1080)
root.config(padx = 20, pady=20)


def Load_File():
    import_file=tkinter.Tk()
    import_file.iconbitmap('STRATV.ico')
    import_file.title('STRAT-V')
    import_file.geometry('500x500')
    import_file.pack_propagate(False)
    #import_file.resizable(0,0)

    #frame for Treeview
    frame3=tkinter.LabelFrame(import_file,text='Data File')
    #frame3.place(height=250, width=500)
    frame3.place(relheight=0.5, relwidth=1)

    #Frame for open filedialog
    file_frame=tkinter.LabelFrame(import_file, text='Open File')
    file_frame.place(height=100, width=500, rely=0.65, relx=0)

    #Buttons
    button1=tkinter.Button(file_frame, text = 'Browse A File',command=lambda:file_dialog())
    button1.place(rely=0.65, relx=0.8)

    button2= tkinter.Button(file_frame, text = 'Load Permeability-Porosity Data', command=lambda: Load_Permeability_Porosity_Data())
    button2.place(rely=0.65,relx=0.4)
    button3=tkinter.Button(file_frame, text = 'Load Relative Permeability Data', command=lambda: Load_Relative_Permeability_Data())
    button3.place(rely=0.65, relx=0)

    label_file = tkinter.Label(file_frame, text = 'No File Selected')
    label_file.place(rely=0,relx=0)

    #Treeview Widget
    tv1=tkinter.Treeview(frame3)
    tv1.place(relheight=1, relwidth=1)

    treescrolly = tkinter.Scrollbar(frame3, orient='vertical',command=tv1.yview)
    treescrollx = tkinter.Scrollbar(frame3, orient='horizontal',command=tv1.xview)
    tv1.configure(xscrollcommand=treescrollx.set)
    tv1.configure(yscrollcommand=treescrolly.set)
    treescrollx.pack(side='bottom', fill='x')
    treescrolly.pack(side='right', fill='y')

    def file_dialog():
        filename= filedialog.askopenfilename(initialdir="/", title = "Select A File", filetype=(("csvfiles","*.csv"),("All Files", "*.*")))
        label_file["text"]=filename

    def Load_Permeability_Porosity_Data():
        file_path=label_file['text']
        try:
            excel_filename=r"{}".format(file_path)
            bed_data=pd.read_csv(excel_filename)
        except ValueError:
            messagebox.showerror("Information","The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            messagebox.showerror("Information", f"No such file as {file_path}")
            return None
        
        clear_data()
        tv1["column"]=list(bed_data.columns)
        tv1['show']='headings'
        for column in tv1['columns']:
            tv1.heading(column,text=column)
        bed_data_rows = bed_data.to_numpy().tolist()
        for row in bed_data_rows:
            tv1.insert("","end", values=row)
            
    def Load_Relative_Permeability_Data():
        file_path=label_file['text']
        try:
            excel_filename=r"{}".format(file_path)
            RPERM_data=pd.read_csv(excel_filename)
        except ValueError:
            messagebox.showerror("Information","The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            messagebox.showerror("Information", f"No such file as {file_path}")
            return None

        clear_data()
        tv1["column"]=list(RPERM_data.columns)
        tv1['show']='headings'
        for column in tv1['columns']:
            tv1.heading(column,text=column)
        RPERM_data_rows = RPERM_data.to_numpy().tolist()
        for row in RPERM_data_rows:
            tv1.insert("","end", values=row)
        return None
    def clear_data():
        tv1.delete(*tv1.get_children())
    import_file.mainloop()


menubar = tkinter.Menu(root)
#Create a load menu
loadmenu = tkinter.Menu(menubar, tearoff=0)
loadmenu.add_command(label="Load Data",command =  Load_File)
menubar.add_cascade(label="Load Data", menu=loadmenu)


root.mainloop()