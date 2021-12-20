from tkinter import *
from tkinter import ttk

Corporation = "Siddhartha Corporation"

class Student():
	def __init__(self,root):
		
		#Geometry
		self.root = root
		self.root.title("{}".format(Corporation))
		self.root.geometry("1370x700")
		self.root.configure(bg="#121212")

		#Variables
		self.roll_var = StringVar()
		self.name_var = StringVar()
		self.email_var = StringVar()
		self.gender_var = StringVar()
		self.contact_var = StringVar()
		self.dob_var = StringVar()
		self.search_by = StringVar()
		self.search_txt = StringVar()

		#Placements
		title =  Label(
			self.root,text="College Management System",
			bd=3,
			relief=GROOVE,
			font=(
				"times new roman",
				50,
				"bold"
				),
			bg="#121212",
			fg="white"
			)

		title.pack(
			side=TOP,
			fill=X
			)

		manage_frame=Frame(
			self.root,
			bd=4,
			relief=RIDGE,
			bg="#121212"
			)

		manage_frame.place(
			x=20,
			y=100,
			width=450,
			height=580
			)

		m_title= Label(
			manage_frame,
			text="Manage Students",
			bd=3,
			bg="#121212",
			fg="white",
			font=(
				"times new roman",
				25,
				"bold"
				)
			)

		m_title.grid(
			row=0,
			columnspan=2,
			pady=20,
			padx=80
			)

		lbl_roll= Label(
			manage_frame,
			text="Roll no",
			bg="#121212",
			fg="white",
			font=(
				"times new roman",
				15,
				"bold"
				)
			)

		lbl_roll.grid(
			row=1,
			column=0,
			pady=10,
			padx=10,
			sticky="w"
			)

		txt_roll= Entry(
			manage_frame,
			textvariable=self.roll_var,
			font=(
				"times new roman",
				15,
				"bold"
				),
			bd=5,
			relief=GROOVE
			)

		txt_roll.grid(
			row=1,
			column=0,
			pady=10,
			padx=85,
			sticky="w"
			)		

		lbl_name= Label(
			manage_frame,
			text="Name",
			bg="#121212",
			fg="white",
			font=(
				"times new roman",
				15,
				"bold"
				)
			)

		lbl_name.grid(
			row=2,
			column=0,
			pady=10,
			padx=10,
			sticky="w"
			)

		txt_name= Entry(
			manage_frame,
			textvariable=self.name_var,
			font=(
				"times new roman",
				15,
				"bold"
				),
			bd=5,
			relief=GROOVE
			)

		txt_name.grid(
			row=2,
			column=0,
			pady=10,
			padx=85,
			sticky="w"
			)		

		lbl_email= Label(
			manage_frame,
			text="Email",
			bg="#121212",
			fg="white",
			font=(
				"times new roman",
				15,
				"bold"
				)
			)

		lbl_email.grid(
			row=3,
			column=0,
			pady=10,
			padx=10,
			sticky="w"
			)

		txt_email= Entry(
			manage_frame,
			textvariable=self.email_var,
			font=(
				"times new roman",
				15,
				"bold"
				),
			bd=5,
			relief=GROOVE
			)

		txt_email.grid(
			row=3,
			column=0,
			pady=10,
			padx=85,
			sticky="w"
			)

		lbl_email= Label(
			manage_frame,
			text="Gender",
			bg="#121212",
			fg="white",
			font=(
				"times new roman",
				15,
				"bold"
				)
			)

		lbl_email.grid(
			row=4,
			column=0,
			pady=10,
			padx=10,
			sticky="w"
			)

		combo_gender= ttk.Combobox(
			manage_frame,
			textvariable=self.gender_var,
			font=(
				"times new roman",
				15,
				"bold"
				),
			state="readonly"
			)

		combo_gender['values'] = (
			"Male",
			"Female",
			"Others"
			)

		combo_gender.place(x=85,
			y=270
			)

		lbl_contact= Label(
			manage_frame,
			text="Contact",
			bg="#121212",
			fg="white",
			font=(
				"times new roman",
				15,
				"bold"
				)
			)

		lbl_contact.grid(
			row=6,
			column=0,
			pady=10,
			padx=10,
			sticky="w"
			)

		txt_contact= Entry(
			manage_frame,
			textvariable=self.contact_var,
			font=(
				"times new roman",
				15,
				"bold"
				),
			bd=5,
			relief=GROOVE
			)

		txt_contact.grid(
			row=6,
			column=0,
			pady=10,
			padx=85,
			sticky="w"
			)

		lbl_dob= Label(
			manage_frame,
			text="D.O.B",
			bg="#121212",
			fg="white",
			font=(
				"times new roman",
				15,
				"bold"
				)
			)

		lbl_dob.grid(
			row=7,
			column=0,
			pady=10,
			padx=10,
			sticky="w"
			)

		txt_dob= Entry(
			manage_frame,
			textvariable=self.dob_var,
			font=(
				"times new roman",
				15,
				"bold"
				),
			bd=5,
			relief=GROOVE
			)

		txt_dob.grid(
			row=7,
			column=0,
			pady=10,
			padx=85,
			sticky="w"
			)

		lbl_add= Label(
			manage_frame,
			text="Address",
			bg="#121212",
			fg="white",
			font=(
				"times new roman",
				15,
				"bold"
				)
			)

		lbl_add.grid(
			row=8,
			column=0,
			pady=10,
			padx=10,
			sticky="w"
			)

		txt_add= Text(
			manage_frame,
			width=20,
			height=2,
			font=(
				"times new roman",
				15,
				"bold"
				),
			bd=5,
			relief=GROOVE
			)

		txt_add.grid(
			row=8,
			column=0,
			pady=10,
			padx=85,
			sticky="w"
			)

		btn_frame=Frame(
			manage_frame,
			bd=3,
			relief=RIDGE,
			bg="#121212"
			)

		btn_frame.place(
			x=6,
			y=505,
			width=430,
			)

		addbtn = Button(
			btn_frame,
			text="Add",
			width=7,
			).grid(
			row=0,
			column=1,
			padx=10,
			pady=10
			)

		updatebtn = Button(
			btn_frame,
			text="Update",
			width=7,
			).grid(
			row=0,
			column=2,
			padx=10,
			pady=10
			)

		clearbtn = Button(
			btn_frame,
			text="Clear",
			width=7,
			).grid(
			row=0,
			column=3,
			padx=10,
			pady=10
			)

		delbtn = Button(
			btn_frame,
			text="Delete",
			width=7,
			).grid(
			row=0,
			column=4,
			padx=10,
			pady=10
			)

		details_frame=Frame(
			self.root,
			bd=4,
			relief=RIDGE,
			bg="#121212"
			)

		details_frame.place(
			x=480,
			y=100,
			width=870,
			height=580
			)

		d_search= Label(
			details_frame,
			text="Search By",
			bd=3,
			bg="#121212",
			fg="white",
			font=(
				"times new roman",
				15,
				"bold"
				)
			)

		d_search.place(
			x=5,
			y=10
			)

		combo_search= ttk.Combobox(
			details_frame,
			textvariable=self.search_by,
			font=(
				"times new roman",
				12,
				"bold"
				),
			state="readonly"
			)

		combo_search['values'] = (
			"Roll no.",
			"Name",
			"Contact"
			)

		combo_search.place(
			x=100,
			y=14
			)

		searchbar= Entry(
			details_frame,
			textvariable=self.search_txt,
			font=(
				"times new roman",
				13,
				"bold"
				),
			bd=5,
			relief=GROOVE
			)

		searchbar.place(
			x=285,
			y=14,
			width= 315,
			height=25
			)
		
		searchbtn = Button(
			details_frame,
			text="Search",
			width=7,
			).place(
			x=610,
			y=14,
			width=75,
			height=25
			)

		showallbtn = Button(
			details_frame,
			text="Show All",
			width=7,
			).place(
			x=690,
			y=14,
			width=75,
			height=25
			)

		Table_frame=Frame(
			details_frame,
			bd=4,
			relief=RIDGE,
			bg="#121212"
			)

		Table_frame.place(
			x=5,
			y=60,
			width=850,
			height=500
			)

		scroll_x= Scrollbar(
			Table_frame,
			orient=HORIZONTAL
			)

		scroll_y= Scrollbar(
			Table_frame,
			orient=VERTICAL
			)

		self.Student_Table=ttk.Treeview(
			Table_frame,
			column=(
				"roll",
				"name",
				"email",
				"gender",
				"contact",
				"dob",
				"address"
				),
			xscrollcommand=scroll_x.set,
			yscrollcommand=scroll_y.set
			)

		scroll_x.pack(
			side=BOTTOM,
			fill=X
			)

		scroll_y.pack(
			side=RIGHT,
			fill=Y
			)

		scroll_x.config()
		scroll_y.config()

		self.Student_Table.heading(
			"roll",
			text="Roll no."
			)

		self.Student_Table.heading(
			"name",
			text="Name"
			)

		self.Student_Table.heading(
			"email",
			text="Email"
			)

		self.Student_Table.heading(
			"gender",
			text="Gender"
			)

		self.Student_Table.heading(
			"contact",
			text="Contact"
			)

		self.Student_Table.heading(
			"dob",
			text="D.O.B"
			)

		self.Student_Table.heading(
			"address",
			text="Address"
			)

		self.Student_Table['show'] = "headings"

		self.Student_Table.column(
			"roll",
			width=100
			)

		self.Student_Table.column(
			"name",
			width=100
			)

		self.Student_Table.column(
			"email",
			width=100
			)

		self.Student_Table.column(
			"gender",
			width=100
			)

		self.Student_Table.column(
			"contact",
			width=100
			)

		self.Student_Table.column(
			"dob",
			width=100
			)

		self.Student_Table.column(
			"address",
			width=150
			)

		self.Student_Table.pack(
			fill=BOTH,
			expand=1
			)


class Student():
	pass
	root = Tk()
	obj  = Student(root)
	root.mainloop()
