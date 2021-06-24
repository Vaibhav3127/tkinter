from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("Database")
root.iconbitmap("C:\\Users\\tupte\\PycharmProjects\\tkinter\\net.ico")
root.geometry("400x600")

# create a database or connect to a database
conn = sqlite3.connect("address_book.db")

# create a cursor
cursor = conn.cursor()

# create a table
'''cursor.execute("""CREATE TABLE addresses(
                first_name text,
                last_name text,
                address text,
                city text,
                state text,
                zipcode integer
                )""")'''


# create a update button
def update():
    # create a database or connect to a database
    conn = sqlite3.connect("address_book.db")

    # create a cursor
    cursor = conn.cursor()

    record_id = del_rec.get()

    cursor.execute("""UPDATE addresses SET
                    first_name=:first,
                    last_name=:second,
                    address=:address,
                    city=:city,
                    state=:state,
                    zipcode=:zipcode
                    
                   WHERE oid=:oid""",
                   {
                       'first': f_name_editor.get(),
                       'second': l_name_editor.get(),
                       'address': address_editor.get(),
                       'city': city_editor.get(),
                       'state': state_editor.get(),
                       'zipcode': zipcode_editor.get(),
                       'oid': record_id
                   })

    # commit changes
    conn.commit()

    # colse connection
    conn.close()

    editor.destroy()


# create a function to edit record
def edit():
    global editor

    editor = Tk()
    editor.title("Update Record")
    editor.iconbitmap("C:\\Users\\tupte\\PycharmProjects\\tkinter\\net.ico")

    # create a database or connect to a database
    conn = sqlite3.connect("address_book.db")

    # create a cursor
    cursor = conn.cursor()

    record_id = del_rec.get()
    cursor.execute("SELECT * FROM addresses WHERE oid= " + record_id)
    records = cursor.fetchall()
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # creating boxes or entry
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    # creating lables
    lab1_editor = Label(editor, text="First Name")
    lab1_editor.grid(column=0, row=0, pady=(10, 0))

    lab2_editor = Label(editor, text="Last Name")
    lab2_editor.grid(column=0, row=1)

    lab3_editor = Label(editor, text="Address")
    lab3_editor.grid(column=0, row=2)

    lab4_editor = Label(editor, text="City")
    lab4_editor.grid(column=0, row=3)

    lab5_editor = Label(editor, text="State")
    lab5_editor.grid(column=0, row=4)

    lab6_editor = Label(editor, text="Zip Code")
    lab6_editor.grid(column=0, row=5)

    update_button_editor = Button(editor, text="Save Records", command=update, bg="green")
    update_button_editor.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=135)

    # loop thru records
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])


# create function to delete a record
def delete():
    # create a database or connect to a database
    conn = sqlite3.connect("address_book.db")

    # create a cursor
    cursor = conn.cursor()

    cursor.execute("DELETE from addresses WHERE oid= " + del_rec.get())
    del_rec.delete(0, END)

    # commit changes
    conn.commit()

    # colse connection
    conn.close()


# create a submit button for database
def submit_data():
    # create a database or connect to a database
    conn = sqlite3.connect("address_book.db")

    # create a cursor
    cursor = conn.cursor()

    cursor.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
                   {
                       'f_name': f_name.get(),
                       'l_name': l_name.get(),
                       'address': address.get(),
                       'city': city.get(),
                       'state': state.get(),
                       'zipcode': zipcode.get()
                   }
                   )
    # commit changes
    conn.commit()

    # colse connection
    conn.close()

    # clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# create quary function
def quary():
    # create a database or connect to a database
    conn = sqlite3.connect("address_book.db")

    # create a cursor
    cursor = conn.cursor()

    cursor.execute("SELECT *,oid FROM addresses")
    records = cursor.fetchall()
    # print(records)

    # loop thru records
    print_record = ""
    for record in records:
        print_record += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    quary_lable = Label(root, text=print_record)
    quary_lable.grid(row=12, column=0, columnspan=2)

    # commit changes
    conn.commit()

    # colse connection
    conn.close()


# creating boxes or entry
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

del_rec = Entry(root, width=40)
del_rec.grid(row=8, column=1, padx=20, pady=5)

# creating lables
lab1 = Label(root, text="First Name")
lab1.grid(column=0, row=0, pady=(10, 0))

lab2 = Label(root, text="Last Name")
lab2.grid(column=0, row=1)

lab3 = Label(root, text="Address")
lab3.grid(column=0, row=2)

lab4 = Label(root, text="City")
lab4.grid(column=0, row=3)

lab5 = Label(root, text="State")
lab5.grid(column=0, row=4)

lab6 = Label(root, text="Zip Code")
lab6.grid(column=0, row=5)

delete_lab = Label(root, text="Select Id")
delete_lab.grid(column=0, row=8, pady=5)

# creating submit button
submit = Button(root, text="Add Record To Database", command=submit_data)
submit.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# create a quary button
quary_button = Button(root, text="Show Records", command=quary)
quary_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=127)

# create a delete button
delete_button = Button(root, text="Delete Records", command=delete)
delete_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=127)

# create update button
update_button = Button(root, text="Edit Records", command=edit)
update_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=135)

exit_but = Button(root, text="Exit", command=root.quit)
exit_but.grid(row=13, column=0, columnspan=2)

# commit changes
conn.commit()

# colse connection
conn.close()

root.mainloop()
