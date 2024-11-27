# Install GUI For Python
# -- PyQt5 : pip3 install PyQt5
# -- Tkinter: pip3 install tkinter
# -- Kivy: pip3 install kivy

# Import TKinter
from tkinter import *
import sqlite3

# BEGIN ================================== Creating Windows ================================== BEGIN
root = Tk()
root.title('Library Management System')
root.geometry("600x400")
root.minsize(600, 250)
root.maxsize(600, 800)
# END ==================================== Creating Windows ==================================== END


# BEGIN ======================================  Frames  ====================================== BEGIN
# Create a frame for the title
title_frame = LabelFrame(root, borderwidth = 0, pady = 5)
title_frame.pack(side = "top", anchor = "center")

# Create a frame for the dropdown menu
dropdown_frame = LabelFrame(root, borderwidth = 5, pady = 0)
dropdown_frame.pack()

# Create a frame for the text fields 
textfield_frame = Frame(root, borderwidth = 0, padx = 5, pady = 5)
textfield_frame.pack(padx = 2)

# Create a frame for the resutls
results_frame = Frame(root, borderwidth = 0, padx = 5, pady = 5)
results_frame.pack(padx = 2)
# END ========================================  Frames  ======================================== END


# BEGIN ================================== Dropdown Options ================================== BEGIN
# Query options for dropdown
query_options = [
	"======== Select Query ========",
	"======== Part 2 Query ========",
	"Part 2 - Query 1",
	"Part 2 - Query 2",
	"Part 2 - Query 3",
	"Part 2 - Query 4a",
	"Part 2 - Query 4b",
	"Part 2 - Query 5",
	"Part 2 - Query 6",
	"Part 2 - Query 7",
	"Part 2 - Query 8",
	"Part 2 - Query 9",
	"Part 2 - Query 10",
	"",
	"======== Part 3 Query ========",
	"Part 3 - Query 1",
	"Part 3 - Query 2",
	"Part 3 - Query 3",
	"",
	"Recreate Database"
]
# END ==================================== Dropdown Options ==================================== END



# BEGIN ================================== Dropdown Command ================================== BEGIN
# Command for selected dropdown menu, where event checks for changes in dropdown
def select_from_dropdown(event):
	for widget in textfield_frame.grid_slaves():
		if int(widget.grid_info()["row"]) > 1:
			widget.grid_forget()

	if clicked.get() == "Part 2 - Query 1":
		# Query 1 - Add New Borrower
		query1_label = Label(textfield_frame, text = "Insert New Borrower Into Database")
		query1_label.grid(row = 3, column = 0, columnspan = 2)

		# Textbox Fields
		bo_name = Entry(textfield_frame, width = 30)
		bo_name.grid(row = 4, column = 1)

		bo_address = Entry(textfield_frame, width = 30)
		bo_address.grid(row = 5, column = 1)

		bo_phone = Entry(textfield_frame, width = 30)
		bo_phone.grid(row = 6, column = 1)

		# Textbox Labels
		bo_name_label = Label(textfield_frame, text = "Borrower's Name")
		bo_name_label.grid(row = 4, column = 0, sticky = "w")

		bo_address_label = Label(textfield_frame, text = "Borrower's Address")
		bo_address_label.grid(row = 5, column = 0, sticky = "w")

		bo_phone_label = Label(textfield_frame, text = "Borrower's Phone")
		bo_phone_label.grid(row = 6, column = 0, sticky = "w")

	elif clicked.get() == "Part 2 - Query 2":
		# Query 2 - Update Phone Number Of Borrower
		query2_label = Label(textfield_frame, text = "Update A Borrower's Phone Number")
		query2_label.grid(row = 3, column = 0, columnspan = 2)

	elif clicked.get() == "Part 2 - Query 3":
		# Query 2 - Update Phone Number Of Borrower
		query3_label = Label(textfield_frame, text = "Increase Number Of Book Copies By 1 In A Branch")
		query3_label.grid(row = 3, column = 0, columnspan = 2)

	elif clicked.get() == "Part 2 - Query 4a":
		# Query 4a - Update Phone Number Of Borrower
		query4a_label = Label(textfield_frame, text = "Insert A New Book With Details Regarding The Book, Publisher, and Author")
		query4a_label.grid(row = 3, column = 0, columnspan = 2)

	elif clicked.get() == "Part 2 - Query 4b":
		# Query 4b - Update Phone Number Of Borrower
		query4b_label = Label(textfield_frame, text = "Insert A New Branch With Branch Details")
		query4b_label.grid(row = 3, column = 0, columnspan = 2)

	else:
		select_label = Label(textfield_frame, text = "Select the query using the dropdown above.")
		select_label.grid(row = 2, column = 0)
# END ==================================== Dropdown Command ==================================== END

# BEGIN ============================== Complete Queries Command ============================== BEGIN
def do_query():
	# Create a frame for the results based on query
	placeholder_label = Label(results_frame)
	if clicked.get() == "Part 2 - Query 1":
		placeholder_label.config(text = "Results For Query 1")
		placeholder_label.grid(row = 3, column = 0, columnspan = 2)
	elif clicked.get() == "Part 2 - Query 2":
		placeholder_label.config(text = "Results For Query 2")
		placeholder_label.grid(row = 3, column = 0, columnspan = 2)
	else:
		placeholder_label.grid_forget()


# END ================================ Complete Queries Command ================================ END

# Labels
# Place title of database system at the top using the frame
# Place title of database system at the top using the frame
title = Label(title_frame, text = "Library Management System",
	  background = "blue", foreground = "white",
	  justify = "center", anchor = "center", padx = 224,
	  pady = 5)
title.grid(row = 0, columnspan = 10)



clicked = StringVar()
clicked.set(query_options[0])

dropdown = OptionMenu(dropdown_frame, clicked, *query_options, command = select_from_dropdown)
dropdown.grid(row = 1)

footer = Label(root, text = "Created By Group 2 - Chime Nguyen, Ivan Ko, Trung Nguyen",
	  background = "blue", foreground = "white",
	  justify = "center", anchor = "center", padx = 224,
	  pady = 5)
footer.pack(side = "bottom", anchor = "center")


# Connect to or create a Library Management System Database and create the tables, if they are not created
conn = sqlite3.connect('library_management_system.db')

# Create a cursor
create_tables = conn.cursor()



# Create Library Management System tables
create_tables.execute("""
    CREATE TABLE IF NOT EXISTS PUBLISHER (
        -- Attributes
        Publisher_Name VARCHAR(27) NOT NULL,
        Phone CHAR(12) NOT NULL,
        Address VARCHAR(120) NOT NULL,

		-- Primary Key & Secondary Keys
        PRIMARY KEY (Publisher_Name)
    )
""")

create_tables.execute("""
    CREATE TABLE IF NOT EXISTS LIBRARY_BRANCH (
		-- Attributes
        Branch_Id INTEGER PRIMARY KEY NOT NULL,
        Branch_Name VARCHAR(11) NOT NULL,
        Branch_Address VARCHAR(120) NOT NULL
    )
""")

create_tables.execute("""
    CREATE TABLE IF NOT EXISTS BORROWER (
		-- Attributes
        Card_No INTEGER PRIMARY KEY NOT NULL,
        Name VARCHAR(64) NOT NULL,
        Address VARCHAR(120) NOT NULL,
        Phone CHAR(12) NOT NULL,

		-- Primary Key & Secondary Keys
        UNIQUE (Phone)
    )
""")

create_tables.execute("""
    CREATE TABLE IF NOT EXISTS BOOK (
        -- Attributes
		Book_Id INTEGER PRIMARY KEY NOT NULL,
        Title VARCHAR (128) NOT NULL,
        Publisher_name VARCHAR(64) NOT NULL,

        -- Foreign Keys & Foreign Key Constraints
		FOREIGN KEY (Publisher_name) REFERENCES PUBLISHER (Publisher_Name)
    )
""")

create_tables.execute("""
    CREATE TABLE IF NOT EXISTS BOOK_LOANS (
        Book_Id INTEGER NOT NULL,
        Branch_Id INTEGER NOT NULL,
        Card_No INTEGER NOT NULL,
        Date_Out TEXT NOT NULL,
        Due_Date TEXT NOT NULL,
        Returned_date TEXT NOT NULL,

		-- Primary Key & Secondary Keys
        PRIMARY KEY (Book_Id, Branch_Id, Card_No),

        -- Foreign Keys & Foreign Key Constraints
		FOREIGN KEY (Book_Id) REFERENCES BOOK (Book_Id) ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY (Branch_Id) REFERENCES LIBRARY_BRANCH (Branch_Id) ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY (Card_No) REFERENCES BORROWER (Card_No) ON UPDATE CASCADE ON DELETE CASCADE
    )
""")

create_tables.execute("""
    CREATE TABLE IF NOT EXISTS BOOK_COPIES (
        Book_Id INTEGER NOT NULL,
        Branch_Id INTEGER NOT NULL,
        No_Of_Copies INT NOT NULL,
        
        -- Primary Key & Secondary Keys
		PRIMARY KEY (Book_Id, Branch_Id),

        -- Foreign Keys & Foreign Key Constraints
		FOREIGN KEY (Book_Id) REFERENCES BOOK (Book_Id) ON UPDATE CASCADE ON DELETE CASCADE, -- Match Book_Id from Book
        FOREIGN KEY (Branch_Id) REFERENCES LIBRARY_BRANCH (Branch_Id) ON UPDATE CASCADE ON DELETE CASCADE -- Match Branch-Id from Library_Branch
    )
""")

create_tables.execute("""
    CREATE TABLE IF NOT EXISTS BOOK_AUTHORS (
        Book_Id INTEGER NOT NULL,
        Author_Name VARCHAR(30),

        -- Primary Key & Secondary Keys
		PRIMARY KEY (Book_Id, Author_Name),

        -- Foreign Keys & Foreign Key Constraints
		FOREIGN KEY (Book_Id) REFERENCES BOOK(Book_Id) ON UPDATE CASCADE ON DELETE CASCADE
    )
""")



# Add Information To The Database
    # def submit():
    # 	submit_conn = sqlite3.connect('library_management_system.db')
    # 	submit_cur = submit_conn.cursor()

    # 	submit_cur.execute("INSERT INTO ADDRESSES VALUES (:fname, :lname, :street, :city, :state, :zcode)",
    # 		{
    # 			'fname': f_name.get(),
    # 			'lname': l_name.get(),
    # 			'street': street.get(),
    # 			'city': city.get(),
    # 			'state': state.get(),
    # 			'zcode': zcode.get(),
    # 		})

    # 	submit_conn.commit()
    # 	submit_conn.close()



# Given city and state return first and last name
    # def input_query():

    # 	iq_conn = sqlite3.connect('library_management_system.db')
    # 	iq_cur = iq_conn.cursor()

    # 	iq_cur.execute("SELECT FIRST_NAME, LAST_NAME FROM ADDRESSES WHERE CITY = ? AND STATE = ?",
    # 					(city.get(), state.get(),)) 


    # 	records = iq_cur.fetchall()

    # 	print(records)

    # 	print_records = ''

    # 	for record in records:
    # 		print_records += str(record[0] + " " + record[1] + "\n")

    # 	iq_label = Label(root, text = print_records)
    # 	iq_label.grid(row = 9, column = 0, columnspan = 2)



# Define all GUI components in the tkinter root window
#pack -- grid -- place 



# Create buttons to access DB
# submit_btn = Button(root, text = "Add Address", command = submit)
# submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# input_query_btn = Button(root, text = "Show Records", command = input_query)
# input_query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# Project 2 Part 2 Queries
# part_2_query_1 = Button(root, text = "Project 2, Query 1", command = )
# part_2_query_1.grid(row = , column = , columnspan = , pady = , padx = , ipadx = )

# part_2_query_2 = Button(root, text = "Project 2, Query 2", command = )
# part_2_query_2.grid(row = , column = , columnspan = , pady = , padx = , ipadx = )

# part_2_query_3 = Button(root, text = "Project 2, Query 3", command = )
# part_2_query_3.grid(row = , column = , columnspan = , pady = , padx = , ipadx = )

# part_2_query_4a = Button(root, text = "Project 2, Query 4a", command = )
# part_2_query_4a.grid(row = , column = , columnspan = , pady = , padx = , ipadx = )

# part_2_query_4b = Button(root, text = "Project 2, Query 4b", command = )
# part_2_query_4b.grid(row = , column = , columnspan = , pady = , padx = , ipadx = )

# part_2_query_5 = Button(root, text = "Project 2, Query 5", command = )
# part_2_query_5.grid(row = , column = , columnspan = , pady = , padx = , ipadx = )

# part_2_query_6 = Button(root, text = "Project 2, Query 6", command = )
# part_2_query_6.grid(row = , column = , columnspan = , pady = , padx = , ipadx = )

# part_2_query_7 = Button(root, text = "Project 2, Query 7", command = )
# part_2_query_7.grid(row = , column = , columnspan = , pady = , padx = , ipadx = )

# part_2_query_8 = Button(root, text = "Project 2, Query 8", command = )
# part_2_query_8.grid(row = , column = , columnspan = , pady = , padx = , ipadx = )

# part_2_query_9 = Button(root, text = "Project 2, Query 9", command = )
# part_2_query_9.grid(row = , column = , columnspan = , pady = , padx = , ipadx = )

# part_2_query_10 = Button(root, text = "Project 2, Query 10", command = )
# part_2_query_10.grid(row = , column = , columnspan = , pady = , padx = , ipadx = )

# Project 2 Part 3 Queries

query_button = Button(root, text = "Complete Query", command = do_query)
query_button.pack()

# Commit changes

# Quit

# Run Main Loop
root.mainloop()