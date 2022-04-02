from tkinter import *
from tkinter import ttk
from func import add_data
from tkinter import messagebox

Corporation = "Siddhartha Corporation"


class Student:
    def __init__(self, root):

        # Geometry
        self.root = root
        self.root.title("{}".format(Corporation))
        self.root.geometry("1370x700")
        self.root.configure(bg="#121212")

        # Variables
        self.roll_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        self.search_txt = StringVar()
        # self.txt_add =  txt_add.get(1.0,END)

        # Functions
        def clearAll():
            txt_roll.delete(0, END)
            txt_name.delete(0, END)
            txt_email.delete(0, END)
            txt_dob.delete(0, END)
            txt_contact.delete(0, END)
            self.txt_add.delete(1.0, END)
            searchbar.delete(0, END)
            combo_search.set("")
            combo_gender.set("")

        def clearTree():
            for item in self.Student_Table.get_children():
                self.Student_Table.delete(item)

        def fetchData():
            try:
                import sqlite3

                con = sqlite3.connect("info.db")
                cur = con.cursor()
                clearTree()
                for row in cur.execute("SELECT * FROM students"):
                    self.Student_Table.insert(
                        "",
                        "end",
                        text="L1",
                        values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]),
                    )
            except:
                pass

        # Button Functionality
        def AddButton():
            # txt_add.get(1.0,END))
            try:
                status = add_data(
                    self.roll_var.get(),
                    self.name_var.get(),
                    self.email_var.get(),
                    self.gender_var.get(),
                    self.contact_var.get(),
                    self.dob_var.get(),
                    self.txt_add.get(1.0, END)
                )
                if status:
                    messagebox.showinfo("SidCorp", message='Added data Successfully')
                else:
                    messagebox.showerror(title="Error", message=f"Roll Number: {self.roll_var.get()} already exists!")
            except Exception as e:
                print(e, "this")
            fetchData()
            clearAll()
            # process = create_table()
            # print(process)
        def ClearButton():
            clearTree()
            clearAll()
        
        def showAll():
            fetchData()

        def updateButton():
            try:
                import sqlite3
                con = sqlite3.connect('info.db')
                cur = con.cursor()
                #getting variables
                primaryKey = self.roll_var.get()
                cur.execute('''UPDATE students SET roll = ?, name = ?, email = ?, gender = ?, contact = ?, dob = ?, address = ?   WHERE roll = ?''', (
                    self.roll_var.get(),
                    self.name_var.get(),
                    self.email_var.get(),
                    self.gender_var.get(),
                    self.contact_var.get(),
                    self.dob_var.get(),
                    self.txt_add.get(1.0, END),
                    primaryKey
                    ))
                con.commit()
                messagebox.showinfo("SidCorp", message='Updated data Successfully')
                clearAll()
                fetchData()
            except Exception as e:
                messagebox.showerror(title="Error", message=f"{e}")

        def deleteButton():
            try:
                import sqlite3
                con = sqlite3.connect('info.db')
                cur = con.cursor()
                cur.execute('''DELETE FROM students WHERE roll = ?''',(self.roll_var.get(),))
                con.commit()
                con.close()
                messagebox.showinfo("SidCorp", message='Deleted data Successfully')
                clearAll()
                fetchData()
            except Exception as e:
                messagebox.showerror(title="Error", message=f"{e}")




                for row in cur.execute("SELECT * FROM students"):
                    self.Student_Table.insert(
                        "",
                        "end",
                        text="L1",
                        values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]),
                    )

        def searchButton():
            mode = self.search_by.get()
            query = self.search_txt.get()
            try:
                import sqlite3
                con = sqlite3.connect('info.db')
                cur = con.cursor()
                if (mode == "" or mode == "Name"):
                    for row in cur.execute("SELECT * FROM students WHERE name=?", (query,)):
                        clearTree()
                        print(row,type(row))
                        self.Student_Table.insert(
                            "",
                            "end",
                            text="L1",
                            values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]),
                        )
                elif(mode == "Roll no."):
                    for row in cur.execute("SELECT * FROM students WHERE roll=?", (query,)):
                        clearTree()
                        self.Student_Table.insert(
                            "",
                            "end",
                            text="L1",
                            values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]),
                        )
                else:
                    for row in cur.execute("SELECT * FROM students WHERE contact=?", (query,)):
                        clearTree()
                        self.Student_Table.insert(
                            "",
                            "end",
                            text="L1",
                            values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]),
                        )
            except Exception as e:
                messagebox.showerror(title="Error", message="{}".format(e))
        
            
        # Placements
        title = Label(
            self.root,
            text="Student Management System",
            bd=3,
            relief=GROOVE,
            font=("times new roman", 50, "bold"),
            bg="#121212",
            fg="white",
        )

        title.pack(side=TOP, fill=X)

        manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="#121212")

        manage_frame.place(x=20, y=100, width=450, height=580)

        m_title = Label(
            manage_frame,
            text="Manage Students",
            bd=3,
            bg="#121212",
            fg="white",
            font=("times new roman", 25, "bold"),
        )

        m_title.grid(row=0, columnspan=2, pady=20, padx=80)

        lbl_roll = Label(
            manage_frame,
            text="Roll no",
            bg="#121212",
            fg="white",
            font=("times new roman", 15, "bold"),
        )

        lbl_roll.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        txt_roll = Entry(
            manage_frame,
            textvariable=self.roll_var,
            font=("times new roman", 15, "bold"),
            bd=5,
            relief=GROOVE,
        )

        txt_roll.grid(row=1, column=0, pady=10, padx=85, sticky="w")

        lbl_name = Label(
            manage_frame,
            text="Name",
            bg="#121212",
            fg="white",
            font=("times new roman", 15, "bold"),
        )

        lbl_name.grid(row=2, column=0, pady=10, padx=10, sticky="w")

        txt_name = Entry(
            manage_frame,
            textvariable=self.name_var,
            font=("times new roman", 15, "bold"),
            bd=5,
            relief=GROOVE,
        )

        txt_name.grid(row=2, column=0, pady=10, padx=85, sticky="w")

        lbl_email = Label(
            manage_frame,
            text="Email",
            bg="#121212",
            fg="white",
            font=("times new roman", 15, "bold"),
        )

        lbl_email.grid(row=3, column=0, pady=10, padx=10, sticky="w")

        txt_email = Entry(
            manage_frame,
            textvariable=self.email_var,
            font=("times new roman", 15, "bold"),
            bd=5,
            relief=GROOVE,
        )

        txt_email.grid(row=3, column=0, pady=10, padx=85, sticky="w")

        lbl_email = Label(
            manage_frame,
            text="Gender",
            bg="#121212",
            fg="white",
            font=("times new roman", 15, "bold"),
        )

        lbl_email.grid(row=4, column=0, pady=10, padx=10, sticky="w")

        combo_gender = ttk.Combobox(
            manage_frame,
            textvariable=self.gender_var,
            font=("times new roman", 15, "bold"),
            state="readonly",
        )

        combo_gender["values"] = ("Male", "Female", "Others")

        combo_gender.place(x=85, y=270)

        lbl_contact = Label(
            manage_frame,
            text="Contact",
            bg="#121212",
            fg="white",
            font=("times new roman", 15, "bold"),
        )

        lbl_contact.grid(row=6, column=0, pady=10, padx=10, sticky="w")

        txt_contact = Entry(
            manage_frame,
            textvariable=self.contact_var,
            font=("times new roman", 15, "bold"),
            bd=5,
            relief=GROOVE,
        )

        txt_contact.grid(row=6, column=0, pady=10, padx=85, sticky="w")

        lbl_dob = Label(
            manage_frame,
            text="D.O.B",
            bg="#121212",
            fg="white",
            font=("times new roman", 15, "bold"),
        )

        lbl_dob.grid(row=7, column=0, pady=10, padx=10, sticky="w")

        txt_dob = Entry(
            manage_frame,
            textvariable=self.dob_var,
            font=("times new roman", 15, "bold"),
            bd=5,
            relief=GROOVE,
        )

        txt_dob.grid(row=7, column=0, pady=10, padx=85, sticky="w")

        lbl_add = Label(
            manage_frame,
            text="Address",
            bg="#121212",
            fg="white",
            font=("times new roman", 15, "bold"),
        )

        lbl_add.grid(row=8, column=0, pady=10, padx=10, sticky="w")

        self.txt_add = Text(
            manage_frame,
            width=20,
            height=2,
            font=("times new roman", 15, "bold"),
            bd=5,
            relief=GROOVE,
        )

        self.txt_add.grid(row=8, column=0, pady=10, padx=85, sticky="w")

        btn_frame = Frame(manage_frame, bd=3, relief=RIDGE, bg="#121212")

        btn_frame.place(
            x=6,
            y=505,
            width=430,
        )

        # Buttons

        addbtn = Button(btn_frame, text="Add", width=7, command=AddButton).grid(
            row=0, column=1, padx=10, pady=10
        )

        updatebtn = Button(
            btn_frame,
            text="Update",
            width=7,
            command=updateButton
        ).grid(row=0, column=2, padx=10, pady=10)

        clearbtn = Button(btn_frame, text="Clear", width=7, command=ClearButton).grid(
            row=0, column=3, padx=10, pady=10
        )

        delbtn = Button(
            btn_frame,
            text="Delete",
            width=7,
            command=deleteButton
        ).grid(row=0, column=4, padx=10, pady=10)

        details_frame = Frame(self.root, bd=4, relief=RIDGE, bg="#121212")

        details_frame.place(x=480, y=100, width=870, height=580)

        d_search = Label(
            details_frame,
            text="Search By",
            bd=3,
            bg="#121212",
            fg="white",
            font=("times new roman", 15, "bold"),
        )

        d_search.place(x=5, y=10)

        combo_search = ttk.Combobox(
            details_frame,
            textvariable=self.search_by,
            font=("times new roman", 12, "bold"),
            state="readonly",
        )

        combo_search["values"] = ("Roll no.", "Name", "Contact")

        combo_search.place(x=100, y=14)

        searchbar = Entry(
            details_frame,
            textvariable=self.search_txt,
            font=("times new roman", 13, "bold"),
            bd=5,
            relief=GROOVE,
        )

        searchbar.place(x=285, y=14, width=315, height=25)

        searchbtn = Button(
            details_frame,
            text="Search",
            width=7,
            command=searchButton
        ).place(x=610, y=14, width=75, height=25)

        showallbtn = Button(
            details_frame,
            text="Show All",
            width=7,
            command=showAll
        ).place(x=690, y=14, width=75, height=25)

        Table_frame = Frame(details_frame, bd=4, relief=RIDGE, bg="#121212")

        Table_frame.place(x=5, y=60, width=850, height=500)

        scroll_x = Scrollbar(Table_frame, orient=HORIZONTAL)

        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)

        self.Student_Table = ttk.Treeview(
            Table_frame,
            column=("roll", "name", "email", "gender", "contact", "dob", "address"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        # ttk.Style().configure("Treeview", background="#121212",
        # foreground="#121212", fieldbackground="#121212")

        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config()
        scroll_y.config()

        self.Student_Table.heading("roll", text="Roll no.")

        self.Student_Table.heading("name", text="Name")

        self.Student_Table.heading("email", text="Email")

        self.Student_Table.heading("gender", text="Gender")

        self.Student_Table.heading("contact", text="Contact")

        self.Student_Table.heading("dob", text="D.O.B")

        self.Student_Table.heading("address", text="Address")

        self.Student_Table["show"] = "headings"

        self.Student_Table.column("roll", width=100)

        self.Student_Table.column("name", width=100)

        self.Student_Table.column("email", width=100)

        self.Student_Table.column("gender", width=100)

        self.Student_Table.column("contact", width=100)

        self.Student_Table.column("dob", width=100)

        self.Student_Table.column("address", width=150)

        self.Student_Table.pack(fill=BOTH, expand=1)
        self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor)

    def get_cursor(self,event):
        
        cursor_row = self.Student_Table.focus()
        content = self.Student_Table.item(cursor_row)
        row = content['values']
        self.roll_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_add.delete(1.0, END)
        self.txt_add.insert(END, row[6])

class Student:
    pass
    root = Tk()
    obj = Student(root)
    root.mainloop()
