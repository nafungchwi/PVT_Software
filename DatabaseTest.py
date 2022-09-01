import tkinter as tk
import sqlite3

root = tk.Tk()
root.title("Using databases with sqlite")

#create a database or connect to one 
conn = sqlite3.connect("address_book.db")

#create a cursor 
c = conn.cursor()

#create a table 
#c.execute("""CREATE TABLE addresses (
 #   first_name text,
 #   last_name text,
 #   address text,
 #   city text,
 #   state text,
 #   zipcode integer
#)""")

#create submit function for database 
def submit():

    #create a database or connect to one 
    conn = sqlite3.connect("address_book.db")

    #create a cursor 
    c = conn.cursor()

    #Insert into table 
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name,:address,:city,:state,:zipcode)",
            {
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'city':city.get(),
                'state':state.get(),
                'zipcode':zipcode.get()
            })

    #commit changes
    conn.commit()

    #close connection 
    conn.close()

    #clear the textboxes 
    f_name.delete(0, tk.END)
    l_name.delete(0,tk.END) 
    address.delete(0, tk.END)
    city.delete(0,tk.END)
    state.delete(0,tk.END)
    zipcode.delete(0,tk.END)

#create query function
def query():
    #create a database or connect to one 
    conn = sqlite3.connect("address_book.db")

    #create a cursor 
    c = conn.cursor()

    #query the database 
    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    #print(records)

    #loop through results
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = tk.Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    #commit changes
    conn.commit()

    #close connection 
    conn.close()

#create textboxes  
f_name = tk.Entry(root,width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = tk.Entry(root,width=30)
l_name.grid(row=1, column=1)

address = tk.Entry(root,width=30)
address.grid(row=2, column=1, padx=20)

city = tk.Entry(root,width=30)
city.grid(row=3, column=1, padx=20)

state = tk.Entry(root,width=30)
state.grid(row=4, column=1, padx=20)

zipcode = tk.Entry(root,width=30)
zipcode.grid(row=5, column=1, padx=20)

#create text box labels 
f_name_label = tk.Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = tk.Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = tk.Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = tk.Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = tk.Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = tk.Label(root, text="Zip Code")
zipcode_label.grid(row=5, column=0)

#create submit button
submit_btn = tk.Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create a query button
query_btn = tk.Button(root, text="Show Records", command=query)
query_btn.grid(row=7,column=0, columnspan=2,pady=10, padx=10, ipadx=137)

#commit changes
conn.commit()

#close connection 
conn.close()

root.mainloop()