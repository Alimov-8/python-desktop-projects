from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

# Main Window
window = Tk()
window.title("Register")


# ================ Databases ====================

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create Cursor
c = conn.cursor()

# Create Table For Database
try:
    c.execute('''CREATE TABLE addresses (
                 first_name text,
                 last_name text,
                 address text,
                 city text,
                 state text,
                 zipcode integer
                 )''')
except sqlite3.OperationalError:
    pass


# Functions

def update():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET 
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        
        WHERE oid = :oid""",
        {
        'first': f_name_ed.get(),
        'last': l_name_ed.get(),
        'address': address_ed.get(),
        'city': city_ed.get(),
        'state': state_ed.get(),
        'zipcode': z_code_ed.get(),
        'oid': record_id
        }
    )

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    # Close the window
    editor.destroy()

def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()

    # Delete Record by ID
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()


def edit():
    global editor
    editor = Tk()
    editor.title("Update Record")

    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()

    # Show Records
    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    print(records)

    # Creating global Variables for text box names
    global f_name_ed
    global l_name_ed
    global address_ed
    global city_ed
    global state_ed
    global z_code_ed

    # Creating Entry Table
    f_name_ed = Entry(editor, width=30, font=("times new roman", 13))
    f_name_ed.grid(row=1, column=1, padx=20, pady=5)
    l_name_ed = Entry(editor, width=30, font=("times new roman", 13))
    l_name_ed.grid(row=2, column=1, pady=5)
    address_ed = Entry(editor, width=30, font=("times new roman", 13))
    address_ed.grid(row=3, column=1, pady=5)
    city_ed = Entry(editor, width=30, font=("times new roman", 13))
    city_ed.grid(row=4, column=1, pady=5)
    state_ed = Entry(editor, width=30, font=("times new roman", 13))
    state_ed.grid(row=5, column=1, pady=5)
    z_code_ed = Entry(editor, width=30, font=("times new roman", 13))
    z_code_ed.grid(row=6, column=1, pady=5)

    # Creating Labels
    space_1_ed = Label(editor, text="   Update", font=("times new roman", 20))
    space_1_ed.grid(row=0, column=0, columnspan=3)
    f_name_label_ed = Label(editor, text="First Name", font=("times new roman", 15))
    f_name_label_ed.grid(row=1, column=0, padx=20)
    l_name_label_ed = Label(editor, text="Last Name", font=("times new roman", 15))
    l_name_label_ed.grid(row=2, column=0)
    address_label_ed = Label(editor, text="Address", font=("times new roman", 15))
    address_label_ed.grid(row=3, column=0)
    city_label_ed = Label(editor, text="City", font=("times new roman", 15))
    city_label_ed.grid(row=4, column=0)
    state_label_ed = Label(editor, text="State", font=("times new roman", 15))
    state_label_ed.grid(row=5, column=0)
    z_code_label_ed = Label(editor, text="ZipCode", font=("times new roman", 15))
    z_code_label_ed.grid(row=6, column=0)

    # Create Save Button
    submit_b_ed = Button(editor, text="Save", command=update,
                      font=("times new roman", 15), bg="black", fg="yellow")
    submit_b_ed.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

    #Loop through Results
    for record in records:
        f_name_ed.insert(0, record[0])
        l_name_ed.insert(0, record[1])
        address_ed.insert(0, record[2])
        city_ed.insert(0, record[3])
        state_ed.insert(0, record[4])
        z_code_ed.insert(0, record[5])


def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()

    # Insert into Table
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :z_code)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'z_code': z_code.get()
              })

    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()

    # Show Records
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    print_records = ""
    for record in records:
        print_records += str(record) + "\n"

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    # Clear text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    state.delete(0, END)
    city.delete(0, END)
    z_code.delete(0, END)


def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()

    # Show Records
    c.execute("SELECT *, oid FROM addresses ")
    records = c.fetchall()
    print(records)

    # Loop for result
    print_records = ""
    for record in records:
        print_records += str(record) + "\n"
    query_l = Label(window, text=print_records)
    query_l.grid(row=13, column=0, columnspan=2, pady=15)

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()


# Creating Entry Table

f_name = Entry(window, width=30, font=("times new roman", 13))
f_name.grid(row=1, column=1, padx=20, pady=5)
l_name = Entry(window, width=30, font=("times new roman", 13))
l_name.grid(row=2, column=1, pady=5)
address = Entry(window, width=30, font=("times new roman", 13))
address.grid(row=3, column=1, pady=5)
city = Entry(window, width=30, font=("times new roman", 13))
city.grid(row=4, column=1, pady=5)
state = Entry(window, width=30, font=("times new roman", 13))
state.grid(row=5, column=1, pady=5)
z_code = Entry(window, width=30, font=("times new roman", 13))
z_code.grid(row=6, column=1, pady=5)
delete_box = Entry(window, width=30, font=("times new roman", 13))
delete_box.grid(row=10, column=1, pady=20)


# Creating Labels
space_1 = Label(window, text="   Register", font=("times new roman", 20))
space_1.grid(row=0, column=0, columnspan=3)
f_name_label = Label(window, text="First Name", font=("times new roman", 15))
f_name_label.grid(row=1, column=0, padx=20)
l_name_label = Label(window, text="Last Name", font=("times new roman", 15))
l_name_label.grid(row=2, column=0)
address_label = Label(window, text="Address", font=("times new roman", 15))
address_label.grid(row=3, column=0)
city_label = Label(window, text="City", font=("times new roman", 15))
city_label.grid(row=4, column=0)
state_label = Label(window, text="State", font=("times new roman", 15))
state_label.grid(row=5, column=0)
z_code_label = Label(window, text="ZipCode", font=("times new roman", 15))
z_code_label.grid(row=6, column=0)
delete_box_label = Label(window, text="Select ID", font=("times new roman", 15))
delete_box_label.grid(row=10, column=0)


# Create Submit Button
submit_b = Button(window, text="Add Record to Database", command=submit,
                  font=("times new roman", 15), bg="grey", fg="white")
submit_b.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)


# Create a Query Button
query_b = Button(window, text="Show Record", command=query, font=("times new roman", 13),
                 bg="green", fg="white")
query_b.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


# Create Delete Button
delete_b = Button(window, text="Delete Record", command=delete, font=("times new roman", 13),
                  bg="red", fg="white")
delete_b.grid(row=11, column=0, columnspan=2, pady=10, ipadx=120)


# Create Select Button
edit_b = Button(window, text=" Update Record ", command=edit, font=("times new roman", 13),
                  bg="blue", fg="white")
edit_b.grid(row=12, column=0, columnspan=2, pady=10, ipadx=120)


# Commit Changes
conn.commit()


# Close Connection
conn.close()


window.mainloop()
