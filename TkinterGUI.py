# Install GUI For Python
# -- PyQt5 : pip3 install PyQt5
# -- Tkinter: pip3 install tkinter
# -- Kivy: pip3 install kivy


# Import TKinter
from tkinter import *
import sqlite3

# Create tkinter window
root = Tk()
root.title('Library Management System')
root.geometry("600x400")
root.minsize(600, 100)
root.maxsize(600, 800)



# Create frame for the title
title_frame = LabelFrame(root, borderwidth = 0, pady = 5)
title_frame.grid(row = 0, columnspan = 10)



# Place title of database system at the top using the frame
title = Label(title_frame, text = "Library Management System",
	  background = "blue", foreground = "white",
	  justify = "center", anchor = "center", padx = 224,
	  pady = 5)
title.pack(side = "top", anchor = "center")



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



# Define all textbox fields
# f_name = Entry(root, width = 30)
# f_name.grid(row = 0, column = 1, padx = 20)

# l_name = Entry(root, width = 30)
# l_name.grid(row = 1, column =1)

# street = Entry(root, width = 30)
# street.grid(row = 2, column =1)

# city = Entry(root, width = 30)
# city.grid(row = 3, column =1)

# state = Entry(root, width = 30)
# state.grid(row = 4, column =1)

# zcode = Entry(root, width = 30)
# zcode.grid(row = 5, column =1)



# Define labels
f_name_label = Label(root, text ='First Name: ')
f_name_label.grid(row = 1, column = 0)

# l_name_label = Label(root, text = 'Last Name: ')
# l_name_label.grid(row = 2, column = 0)

# street_label = Label(root, text = 'Street: ')
# street_label.grid(row = 3, column = 0)

# city_label = Label(root, text = 'City: ')
# city_label.grid(row = 4, column = 0, sticky = "w")

# state_label = Label(root, text = 'State: ')
# state_label.grid(row = 5, column = 0)

# zcode_label = Label(root, text = 'Zipcode: ')
# zcode_label.grid(row = 6, column = 0)



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


# Commit changes

# Quit

# Run Main Loop
root.mainloop()