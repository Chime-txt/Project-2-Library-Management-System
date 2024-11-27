# Install GUI For Python
# -- PyQt5 : pip3 install PyQt5
# -- Tkinter: pip3 install tkinter
# -- Kivy: pip3 install kivy

# Import TKinter
from tkinter import *
import sqlite3

# BEGIN ======================================== TODO ======================================== BEGIN
# TODO: Create A Database That Can Automatically Create The Tables And Add Data From CSV Files
# TODO: Add Appropreate Text Fields And Labels From Attribute Labels And Attribute Entries Below
# TODO: Rewrite Queries That Generalizes All Queries With The VALUES Or WHERE Clauses
# END ========================================== TODO ========================================++ END


# BEGIN ================================ Query Generalization ================================ BEGIN
# All queries below are written to be generalized, such that the user can input any vaild data and
# it can return a result without errors
# More specifically, any queries that involve a WHERE clause are required to be generalized
# END ================================== Query Generalization ================================++ END


# BEGIN ================================== Rows Information ================================== BEGIN
# Row 0 = Unused
# Row 1 = Dropdown Menu (Reserved)
# Row 2 = Query Select Label (Reserved)
# Row 3 = Unused, Could Be Used To Describe Inputs (Cleared Upon Selecting New Query)
# Rows 4 Onwards = Query Text Fields, Labels, And Results (Cleared Upon Selecting New Query)
# END ==================================== Rows Information ==================================== END


# BEGIN ================================== Creating Windows ================================== BEGIN
root = Tk()
root.title('Library Management System')
root.geometry("600x400")
root.minsize(600, 250)
root.maxsize(600, 800)
# END ==================================== Creating Windows ==================================== END


# BEGIN ======================================  Frames  ====================================== BEGIN
# Create a frame for the dropdown menu
dropdown_frame = LabelFrame(root, borderwidth = 5, pady = 0)

# Create a frame for the text fields 
textfield_frame = Frame(root, borderwidth = 0, padx = 5, pady = 5)

# Create a frame for the resutls
results_frame = Frame(root, borderwidth = 0, padx = 5, pady = 5)
# END ========================================  Frames  ======================================== END


# BEGIN ================================== Dropdown Options ================================== BEGIN
# Query options for dropdown
query_options = [
	"======== Select Query ========",	# query_options[0]
	"======== Part 2 Query ========",	# query_options[1]
	"Part 2 - Query 1",					# query_options[2]
	"Part 2 - Query 2",					#      ...     [3]
	"Part 2 - Query 3",					#      ...     [4]
	"Part 2 - Query 4a",				#      ...     [5]
	"Part 2 - Query 4b",				#      ...     [6]
	"Part 2 - Query 5",					#      ...     [7]
	"Part 2 - Query 6",					#      ...     [8]
	"Part 2 - Query 7",					#      ...     [9]
	"Part 2 - Query 8",					#      ...     [10]
	"Part 2 - Query 9",					#      ...     [11]
	"Part 2 - Query 10",				#      ...     [12]
	"",									#      ...     [13]
	"======== Part 3 Query ========",	#      ...     [14]
	"Part 3 - Query 1",					# query_options[15]
	"Part 3 - Query 2",					#      ...     [16]
	"Part 3 - Query 3",					#      ...     [17]
	# RESETING DATABASE is purely optional and for quick testing purposes
	"",									#      ...     [18]
	"======= RESET DATABASE =======",	#      ...     [19]
	"Reset Database"					# query_options[20]
]
# END ==================================== Dropdown Options ==================================== END


# BEGIN ================================== Dropdown Command ================================== BEGIN
# Command for selected dropdown menu, where event checks for changes in dropdown
# General Dropdown Selection Creator: Chime Nguyen
def select_from_dropdown(event):
	# Remove previous query details
	for widget in textfield_frame.grid_slaves():
		if int(widget.grid_info()["row"]) > 2:
			widget.grid_forget()

	# Clear query results
	results_label.config(text = "")

	if clicked.get() == query_options[2]:
		# Part 2 - Query 1 - Add New Borrower
		query_select_label.config( text = "Insert New Borrower Into Database")

		# Textbox Fields Locations
		bo_name_entry.grid(row = 4, column = 1)
		bo_address_entry.grid(row = 5, column = 1)
		bo_phone_entry.grid(row = 6, column = 1)

		# Textbox Labels Location
		bo_name_label.grid(row = 4, column = 0, sticky = "w")
		bo_address_label.grid(row = 5, column = 0, sticky = "w")
		bo_phone_label.grid(row = 6, column = 0, sticky = "w")
		return
	elif clicked.get() == query_options[3]:
		# Part 2 - Query 2 - Update Phone Number Of Borrower
		query_select_label.config(text = "Update A Borrower's Phone Number")

		# Textbox Fields Locations

		# Textbox Labels Location

		return
	elif clicked.get() == query_options[4]:
		# Part 2 - Query 3 - Add 1 To Book Copies In A Branch
		query_select_label.config(text = "Increase Number Of Book Copies By 1 In A Branch")

		# Textbox Fields Locations

		# Textbox Labels Location
		
		return
	elif clicked.get() == query_options[5]:
		# Part 2 - Query 4a - Add New Book With Details
		query_select_label.config(text = "Insert A New Book With Details Regarding The Book, Publisher, and Author")

		# Textbox Fields Locations

		# Textbox Labels Location
		
		return
	elif clicked.get() == query_options[6]:
		# Part 2 - Query 4b - Add New Branch With Details
		query_select_label.config(text = "Insert A New Branch With Branch Details")

		# Textbox Fields Locations

		# Textbox Labels Location
		
		return
	elif clicked.get() == query_options[7]:
		# Part 2 - Query 5 - Loaned Books Between Two Dates With Details
		query_select_label.config(text = "Find Books That Were Loaned Between Two Dates With Details")

		# Textbox Fields Locations

		# Textbox Labels Location
		
		return
	elif clicked.get() == query_options[8]:
		# Part 2 - Query 6 - List Borrowers Name Based On Return Date
		query_select_label.config(text = "Find Borrowers Based On Book's Return Date")

		# Textbox Fields Locations

		# Textbox Labels Location
		
		return
	elif clicked.get() == query_options[9]:
		# Part 2 - Query 7 - Report All Branches Book Loan Count
		query_select_label.config(text = "Create A Report On Each Branch's Book Loan Count")

		# Textbox Fields Locations
		# May not be necessary due to no VALUES or WHERE clause

		# Textbox Labels Location
		# May not be necessary due to no VALUES or WHERE clause
		
		return
	elif clicked.get() == query_options[10]:
		# Part 2 - Query 8 - List Book Titles With Max Days
		query_select_label.config(text = "List Books Based On How Long The Book Has Been Checked Out For")

		# Textbox Fields Locations
		# May not be necessary due to no VALUES or WHERE clause

		# Textbox Labels Location
		# May not be necessary due to no VALUES or WHERE clause
		
		return
	elif clicked.get() == query_options[11]:
		# Part 2 - Query 9 - Report On A Borrower With All Books That Were Checked Out
		query_select_label.config(text = "Create A Report On A Borrower With All Of Thr Book Loan Details")

		# Textbox Fields Locations

		# Textbox Labels Location
		
		return
	elif clicked.get() == query_options[12]:
		# Part 2 - Query 10 - List Borrowers In Branch Who Borrowed A Book
		query_select_label.config(text = "List All Borrowers In A Branch Who Borrowed At Least One Book")

		# Textbox Fields Locations

		# Textbox Labels Location
		
		return
	elif clicked.get() == query_options[15]:
		# Part 3 - Query 1 - Add Late Attribute In Book Loan Table
		query_select_label.config(text = "Add A Value For Late Books To Book Loan Table")

		# Textbox Fields Locations

		# Textbox Labels Location
		
		return
	elif clicked.get() == query_options[16]:
		# Part 3 - Query 2 - Add Late Fee Attribute In Library Branch Table With Set Fees
		query_select_label.config(text = "Add A Late Fee To The Library Branch Table With Determined Fees")

		# Textbox Fields Locations

		# Textbox Labels Location
		
		return
	elif clicked.get() == query_options[17]:
		# Part 3 - Query 3 - View All Details About A Book Loan
		query_select_label.config(text = "View All Details About A Book Loan")

		# Textbox Fields Locations

		# Textbox Labels Location
		
		return
	else:
		query_select_label.config(text = "Select the query using the dropdown above.")
		return

# Set the dropdown query to the first option in the dropdown
clicked = StringVar()
clicked.set(query_options[0])

# Create a dropdown menu that will change the query view based on what query you are currently on
dropdown = OptionMenu(dropdown_frame, clicked, *query_options, command = select_from_dropdown)
dropdown.grid(row = 1)
# END ==================================== Dropdown Command ==================================== END


# BEGIN ================================== Query  Functions ================================== BEGIN
def part2_query1(query_runner):
	# Variable for the phone max length
	phone_length = 12

	# Verify that any of the data being inserted into is not empty or invalid
	verified = True
	invalid_message = "The following information is missing/invalid: "

	verify_entry = bo_name_entry.get()
	if not verify_entry:
		verified = False
		invalid_message += "Borrower's Name. "
	verify_entry = bo_address_entry.get()
	if not verify_entry:
		verified = False
		invalid_message += "Borrower's Address. "
	verify_entry = bo_phone_entry.get()
	if not verify_entry:
		verified = False
		invalid_message += "Borrower's Phone."
	if len(verify_entry) > phone_length:
		verified = False
		invalid_message += "Borrower's Phone Is Too Long."

	# Return if the inputs are not valid
	if not verified:
		return invalid_message

	# Insert the filled in data into the database after verifying that the data is valid
	query_runner.execute("INSERT INTO BORROWER (Name, Address, Phone) VALUES (:name, :address, :phone)",
					  {
						  'name': bo_name_entry.get(),
						  'address': bo_address_entry.get(),
						  'phone': bo_phone_entry.get()
					  })
	
	# Clear all entries that were used
	bo_name_entry.delete(0, END)
	bo_address_entry.delete(0, END)
	bo_phone_entry.delete(0, END)

	# Return a message that the query was successfully inserted into the table.
	return "Successfully Inserted New Borrower"
	
# END ==================================== Query  Functions ==================================== END


# BEGIN ============================== Complete Queries Command ============================== BEGIN
# General Do Query Creator: Chime Nguyen
def do_query():
	# Create a new connection dedicated to the queries
	query_conn = sqlite3.connect('library_management_system.db')

	# Use this cursor to run the query
	query_runner = query_conn.cursor()

	# Create a frame for the results based on query
	if clicked.get() == query_options[2]:
		# Do computations for Part 2 - Query 1
		results_text = part2_query1(query_runner)
		results_label.config(text = results_text)
		results_label.grid(row = 100, column = 0, columnspan = 2)
	elif clicked.get() == query_options[3]:
		# Do computations for Part 2 - Query 2
		results_label.config(text = "Results For Part 2 - Query 2")
		results_label.grid(row = 100, column = 0, columnspan = 2)
	elif clicked.get() == query_options[4]:
		# Do computations for Part 2 - Query 3
		results_label.config(text = "Results For Part 2 - Query 3")
		results_label.grid(row = 100, column = 0, columnspan = 2)
	elif clicked.get() == query_options[5]:
		# Do computations for Part 2 - Query 4a
		results_label.config(text = "Results For Part 2 - Query 4a")
		results_label.grid(row = 100, column = 0, columnspan = 2)
	elif clicked.get() == query_options[6]:
		# Do computations for Part 2 - Query 4b
		results_label.config(text = "Results For Part 2 - Query 4b")
		results_label.grid(row = 100, column = 0, columnspan = 2)
	elif clicked.get() == query_options[7]:
		# Do computations for Part 2 - Query 5
		results_label.config(text = "Results For Part 2 - Query 5")
		results_label.grid(row = 100, column = 0, columnspan = 2)
	elif clicked.get() == query_options[8]:
		# Do computations for Part 2 - Query 6
		results_label.config(text = "Results For Part 2 - Query 6")
		results_label.grid(row = 100, column = 0, columnspan = 2)
	elif clicked.get() == query_options[9]:
		# Do computations for Part 2 - Query 7
		results_label.config(text = "Results For Part 2 - Query 7")
		results_label.grid(row = 100, column = 0, columnspan = 2)
	elif clicked.get() == query_options[10]:
		# Do computations for Part 2 - Query 8
		results_label.config(text = "Results ForPart 2 -  Query 8")
		results_label.grid(row = 100, column = 0, columnspan = 2)
	elif clicked.get() == query_options[11]:
		# Do computations for Part 2 - Query 9
		results_label.config(text = "Results For Part 2 - Query 9")
		results_label.grid(row = 100, column = 0, columnspan = 2)
	elif clicked.get() == query_options[12]:
		# Do computations for Part 2 - Query 10
		results_label.config(text = "Results For Part 2 - Query 10")
		results_label.grid(row = 100, column = 0, columnspan = 2)
	elif clicked.get() == query_options[15]:
		# Do computations for Part 3 - Query 1
		results_label.config(text = "Results For Part 3 - Query 1")
		results_label.grid(row = 100, column = 0, columnspan = 2)
	elif clicked.get() == query_options[16]:
		# Do computations for Part 3 - Query 2
		results_label.config(text = "Results For Part 3 - Query 2")
		results_label.grid(row = 100, column = 0, columnspan = 2)
	elif clicked.get() == query_options[17]:
		# Do computations for Part 3 - Query 3
		results_label.config(text = "Results For Part 3 - Query 3")
		results_label.grid(row = 100, column = 0, columnspan = 2)
	else:
		results_label.config(text = "")

	# Commit any changes to the database
	query_conn.commit()

	# Close the connection for the query
	query_conn.close()
# END ================================ Complete Queries Command ================================ END




# Add Information To The Database
#     def submit():
#     	submit_conn = sqlite3.connect('library_management_system.db')
#     	submit_cur = submit_conn.cursor()

#     	submit_cur.execute("INSERT INTO ADDRESSES VALUES (:fname, :lname, :street, :city, :state, :zcode)",
#     		{
#     			'fname': f_name.get(),
#     			'lname': l_name.get(),
#     			'street': street.get(),
#     			'city': city.get(),
#     			'state': state.get(),
#     			'zcode': zcode.get(),
#     		})

#     	submit_conn.commit()
#     	submit_conn.close()

# Given city and state return first and last name
#     def input_query():

#     	iq_conn = sqlite3.connect('library_management_system.db')
#     	iq_cur = iq_conn.cursor()

#     	iq_cur.execute("SELECT FIRST_NAME, LAST_NAME FROM ADDRESSES WHERE CITY = ? AND STATE = ?",
#     					(city.get(), state.get(),)) 


#     	records = iq_cur.fetchall()

#     	print(records)

#     	print_records = ''

#     	for record in records:
#     		print_records += str(record[0] + " " + record[1] + "\n")

#     	iq_label = Label(root, text = print_records)
#     	iq_label.grid(row = 9, column = 0, columnspan = 2)



# BEGIN =================================== Table Creation =================================== BEGIN
def create_library_tables():
	# Using our knowledge from Programming Languages, we could check if the database exists, but we may not need to here
	# Connect to or create a Library Management System Database and create the tables, if they are not created
	conn = sqlite3.connect('library_management_system.db')

	# Create a cursor to create the tables
	create_tables = conn.cursor()

	# Creates a PUBLISHER table if it does not exists
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
	print ('Created PUBLISHER table successfully')

	# Creates a LIBRARY_BRANCH table if it does not exists
	create_tables.execute("""
		CREATE TABLE IF NOT EXISTS LIBRARY_BRANCH (
			-- Attributes
			Branch_Id INTEGER PRIMARY KEY NOT NULL,
			Branch_Name VARCHAR(11) NOT NULL,
			Branch_Address VARCHAR(120) NOT NULL
		)
	""")
	print ('Created LIBRARY_BRANCH table successfully')

	# Creates a BORROWER table if it does not exists
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
	print ('Created BORROWER table successfully')

	# Creates a BOOK table if it does not exists
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
	print ('Created BOOK table successfully')

	# Creates a BOOK_LOANS table if it does not exists
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
	print ('Created BOOK_LOANS table successfully')

	# Creates a BOOK_COPIES table if it does not exists
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
	print ('Created BOOK_COPIES table successfully')

	# Creates a BOOK_AUTHORS table if it does not exists
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
	print ('Created BOOK_AUTHORS table successfully')

	# Commit changes
	conn.commit()

	# Quit
	conn.close()

# Creates all of the tables in the library database
create_library_tables()
# END ===================================== Table Creation ===================================== END


# BEGIN ==================================== Query Button ==================================== BEGIN
# This button will run a function called do_query and check against all of the queries before doing
# the selected query, if it is a query
query_button = Button(root, text = "Complete Query", command = do_query)
# END ====================================== Query Button ====================================== END


# Define all GUI components in the tkinter root window
#pack -- grid -- place 


# BEGIN ================================== Attribute Labels ================================== BEGIN
# Place title of database system at the top using the frame
title = Label(root, text = "Library Management System",
	  background = "blue", foreground = "white",
	  justify = "center", anchor = "center", padx = 500,
	  pady = 5)

# The query select label displays the current query or a message asking the user to select a query
# Start by showing a message to tell the user to select a query
query_select_label = Label(textfield_frame, text = "Select the query using the dropdown above.")
# Since the message will always be in a fixed location, we will not need to modify the location
query_select_label.grid(row = 2, column = 0, columnspan = 2)

# The results label will display the results of the query in the results frame
results_label = Label(results_frame)
# The results label position on the grid will be dealt with by the do query function as it will
# be automatically cleared when switching to a different query question

# Place footer of database system at the bottom using the root
footer = Label(root, text = "Created By Group 2 - Chime Nguyen, Ivan Ko, Trung Nguyen",
	  background = "blue", foreground = "white",
	  justify = "center", anchor = "center", padx = 500,
	  pady = 5)

# These are all of the labels for the attributes from the PUBLISHER table
# Not all attributes may be used here
p_publisher_name_label = Entry(textfield_frame, text = "Publisher's Name", width = 30)
p_phone_label = Entry(textfield_frame, text = "Publisher's Phone", width = 30)
p_address_label = Entry(textfield_frame, text = "Publisher's Address", width = 30)

# These are all of the labels for the attributes from the LIBRARY_BRANCH table
# Not all attributes may be used here
lb_branch_id_label = Entry(textfield_frame, text = "Library Branch ID", width = 30)
lb_branch_name_label = Entry(textfield_frame, text = "Library Branch's Name", width = 30)
lb_branch_address_label = Entry(textfield_frame, text = "Library Branch's Address", width = 30)

# These are all of the labels for the attributes from the BORROWER table
# Not all attributes may be used here
bo_name_label = Label(textfield_frame, text = "Borrower's Name", width = 30)
bo_address_label = Label(textfield_frame, text = "Borrower's Address", width = 30)
bo_phone_label = Label(textfield_frame, text = "Borrower's Phone", width = 30)

# These are all of the labels for the attributes from the BOOK table
# Not all attributes may be used here
b_book_id_label = Entry(textfield_frame, text = "Book ID", width = 30)
b_title_label = Entry(textfield_frame, text = "Book Title", width = 30)
b_publisher_name_label = Entry(textfield_frame, text = "Book Publisher's Name", width = 30)

# These are all of the labels for the attributes from the BOOK_LOANS table
# Not all attributes may be used here
bl_book_id_label = Entry(textfield_frame, text = "Book ID", width = 30)
bl_branch_id_label = Entry(textfield_frame, text = "Library Branch ID", width = 30)
bl_card_no_label = Entry(textfield_frame, text = "Borrower Card No", width = 30)
bl_date_out_label = Entry(textfield_frame, text = "Date Out", width = 30)
bl_due_date_label = Entry(textfield_frame, text = "Due Date", width = 30)
bl_returned_date_label = Entry(textfield_frame, text = "Return Date", width = 30)

# These are all of the labels for the attributes from the BOOK_COPIES table
# Not all attributes may be used here
bc_book_id_label = Entry(textfield_frame, text = "Book ID", width = 30)
bc_branch_id_label = Entry(textfield_frame, text = "Library Branch ID", width = 30)
bc_no_of_copies_label = Entry(textfield_frame, text = "Number Of Copies", width = 30)

# These are all of the labels for the attributes from the BOOK_AUTHORS table
# Not all attributes may be used here
ba_book_id_label = Entry(textfield_frame, text = "Book ID", width = 30)
ba_author_name_label = Entry(textfield_frame, text = "Author's Name", width = 30)

# END ==================================== Attribute Labels ==================================== END


# BEGIN ================================= Attribute  Entries ================================= BEGIN
# These are all of the entries for the attributes from the PUBLISHER table
# Not all attributes may be used here
p_publisher_name_entry = Entry(textfield_frame, width = 30)
p_phone_entry = Entry(textfield_frame, width = 30)
p_address_entry = Entry(textfield_frame, width = 30)

# These are all of the entries for the attributes from the LIBRARY_BRANCH table
# Not all attributes may be used here
lb_branch_id_entry = Entry(textfield_frame, width = 30)
lb_branch_name_entry = Entry(textfield_frame, width = 30)
lb_branch_address_entry = Entry(textfield_frame, width = 30)

# These are all of the entries for the attributes from the BORROWER table
# Not all attributes may be used here
bo_name_entry = Entry(textfield_frame, width = 30)
bo_address_entry = Entry(textfield_frame, width = 30)
bo_phone_entry = Entry(textfield_frame, width = 30)

# These are all of the entries for the attributes from the BOOK table
# Not all attributes may be used here
b_book_id_entry = Entry(textfield_frame, width = 30)
b_title_entry = Entry(textfield_frame, width = 30)
b_publisher_name_entry = Entry(textfield_frame, width = 30)

# These are all of the entries for the attributes from the BOOK_LOANS table
# Not all attributes may be used here
bl_book_id_entry = Entry(textfield_frame, width = 30)
bl_branch_id_entry = Entry(textfield_frame, width = 30)
bl_card_no_entry = Entry(textfield_frame, width = 30)
bl_date_out_entry = Entry(textfield_frame, width = 30)
bl_due_date_entry = Entry(textfield_frame, width = 30)
bl_returned_date_entry = Entry(textfield_frame, width = 30)

# These are all of the entries for the attributes from the BOOK_COPIES table
# Not all attributes may be used here
bc_book_id_entry = Entry(textfield_frame, width = 30)
bc_branch_id_entry = Entry(textfield_frame, width = 30)
bc_no_of_copies_entry = Entry(textfield_frame, width = 30)

# These are all of the entries for the attributes from the BOOK_AUTHORS table
# Not all attributes may be used here
ba_book_id_entry = Entry(textfield_frame, width = 30)
ba_author_name_entry = Entry(textfield_frame, width = 30)
# END =================================== Attribute  Entries =================================== END


# BEGIN =================================== Packing  Order =================================== BEGIN
# Pack the title at the top of the window
title.pack(side = "top", anchor = "center")
dropdown_frame.pack()
textfield_frame.pack(padx = 2)
query_button.pack()
results_frame.pack(padx = 2)
# Pack the footer at the bottom of the window
footer.pack(side = "bottom", anchor = "center")
# END ===================================== Packing  Order ===================================== END

# Run Main Loop
root.mainloop()