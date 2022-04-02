from tkinter import ttk
import sqlite3
con = sqlite3.connect('info.db')

cur = con.cursor()


def create_table():
    cur.execute('''CREATE TABLE students
               (roll PRIMARY KEY, name text, email text, gender text, contact text, dob text, address text)''')
    con.commit()

def add_data(roll, name, email, gender, contact, dob, address):
    try:
        create_table()
        add_data(roll, name, email, gender, contact, dob, address)
        return(True)
    except:
        try:
            cur.execute("insert into students values (?, ?, ?, ?, ?, ?, ?)", (roll, name, email, gender, contact, dob, address))
            con.commit()
            return(True)
        except sqlite3.IntegrityError:
            return(False)



# def add_data(roll, name, email, gender, contact, dob, address):
#     try:
#         # Create table
#         cur.execute('''CREATE TABLE students
#                (roll PRIMARY KEY, name text, email text, gender text, contact text, dob text, address text)''')
#         # Insert a row of data      
        # cur.execute("insert into students values (?, ?, ?, ?, ?, ?, ?)", (roll, name, email, gender, contact, dob, address))
        # con.commit()
#     except:       
#         # Insert a row of data
#         cur.execute("insert into students values (?, ?, ?, ?, ?, ?, ?)", (roll, name, email, gender, contact, dob, address))
#         con.commit()
        
        