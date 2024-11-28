# Install GUI For Python
# -- PyQt5 : pip3 install PyQt5
# -- Tkinter: pip3 install tkinter
# -- Kivy: pip3 install kivy

# Import TKinter
from tkinter import *
import sqlite3
import csv
import os

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
root.geometry("600x600")
root.minsize(600, 600)
root.maxsize(600, 900)
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



# BEGIN ================================= Constant Variables ================================= BEGIN
# Note: There is no such thing as a constant variable in Python, but it is written in ALL CAPS to
#		signify that the value should not be modified
PHONE_LENGTH = 12	# Length of phone number (At least in most countries)
RESULTS_ROW = 500	# The row that displays the results (Can be replaced by using pack in future)
MAX_COLUMNSPAN = 10	# Length that the column can span across other columns for
# BEGIN ================================== Dropdown Command ================================== BEGIN



# BEGIN ================================== Dropdown Command ================================== BEGIN
# Command for selected dropdown menu, where event checks for changes in dropdown
# General Dropdown Selection Creator: Chime Nguyen
def select_from_dropdown(event):
	# Remove previous query details
	for widget in textfield_frame.grid_slaves():
		if int(widget.grid_info()["row"]) > 2:
			widget.grid_forget()

	# Remove previous results details
	for widget in results_frame.grid_slaves():
		widget.grid_forget()

	# Clear query results
	results_label.config(text = "")

	if clicked.get() == query_options[2]:		# Part 2 - Query 1
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
	elif clicked.get() == query_options[3]:		# Part 2 - Query 2
		# Part 2 - Query 2 - Update Phone Number Of Borrower
		query_select_label.config(text = "Update A Borrower's Phone Number")

		# Textbox Fields Locations
		bo_phone_entry.grid(row = 4, column = 1)
		bo_name_entry.grid(row = 6, column = 1)

		# Textbox Labels Location
		bo_phone_label.grid(row = 4, column = 0)
		where_label = Label(textfield_frame, text = "Who Are You Updating?")
		where_label.grid(row = 5, columnspan = MAX_COLUMNSPAN)
		bo_name_label.grid(row = 6, column = 0)

		return
	elif clicked.get() == query_options[4]:		# Part 2 - Query 3
		# Part 2 - Query 3 - Add 1 To Book Copies In A Branch
		query_select_label.config(text = "Increase Number Of Book Copies In A Branch")

		# Textbox Fields Locations
		bc_branch_id_entry.grid(row = 4, column = 1)
		bc_no_of_copies_entry.grid(row = 5, column = 1)

		# Textbox Labels Location
		branch_name_or_id_label = Label(textfield_frame, text = "Library Branch's Name or ID", width = 30)
		branch_name_or_id_label.grid(row = 4, column = 0, sticky = "w")
		bc_no_of_copies_label.grid(row = 5, column = 0, sticky = "w")
		
		return
	elif clicked.get() == query_options[5]:
		# Part 2 - Query 4a - Add New Book With Details
		query_select_label.config(text = "Insert A New Book With Details Regarding The Book, Publisher, and Author")

		# Textbox Fields Locations
		b_title_entry.grid(row = 4, column = 1)
		ba_author_name_entry.grid(row = 5, column = 1)
		b_publisher_name_entry.grid(row = 6, column = 1)

		# Textbox Labels Location
		b_title_label.grid(row = 4, column = 0, sticky = "w")
		ba_author_name_label.grid(row = 5, column = 0, sticky = "w")
		b_publisher_name_label.grid(row = 6, column = 0, sticky = "w")

		return
	elif clicked.get() == query_options[6]:
		# Part 2 - Query 4b - Add New Branch With Details
		query_select_label.config(text = "Insert A New Branch With Branch Details")

		# Textbox Fields Locations
		lb_branch_name_entry.grid(row = 4, column = 1)
		lb_branch_address_entry.grid(row = 5, column = 1)

		# Textbox Labels Location
		lb_branch_name_label.grid(row = 4, column = 0, sticky = "w")
		lb_branch_address_label.grid(row = 5, column = 0, sticky = "w")

		return
	elif clicked.get() == query_options[7]:
		# Part 2 - Query 5 - Loaned Books Between Two Dates With Details
		query_select_label.config(text = "Find Books That Were Loaned Between Two Dates With Details")

		# Textbox Fields Locations
		bl_date_out_start_entry.grid(row = 4, column = 1)
		bl_date_out_end_entry.grid(row = 5, column = 1)

		# Textbox Labels Location
		bl_date_out_start_label = Label(textfield_frame, text = "Start Date (YYYY-MM-DD)")
		bl_date_out_start_label.grid(row = 4, column = 0, sticky = "w")
	
		bl_date_out_end_label = Label(textfield_frame, text = "End Date (YYYY-MM-DD)")
		bl_date_out_end_label.grid(row = 5, column = 0, sticky = "w")
		
		
		return
	elif clicked.get() == query_options[8]:		# Part 2 - Query 6
		# Part 2 - Query 6 - List Borrowers Name Based On Return Date
		query_select_label.config(text = "Find Borrowers Based On Book's Return Date")

		# Textbox Fields Locations
		bl_returned_date_entry.grid(row = 4, column = 1)

		# Textbox Labels Location
		bl_returned_date_label.grid(row = 4, column = 0, sticky = "w")
		
		return
	elif clicked.get() == query_options[9]:		# Part 2 - Query 7
		# Part 2 - Query 7 - Report All Branches Book Loan Count
		query_select_label.config(text = "Create A Report On Each Branch's Book Loan Count")

		# Textbox Fields Locations
		# May not be necessary due to no VALUES or WHERE clause

		# Textbox Labels Location
		# May not be necessary due to no VALUES or WHERE clause
		
		return
	elif clicked.get() == query_options[10]:	# Part 2 - Query 8
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
		bo_name_entry.grid(row = 4, column = 1)
		# Textbox Labels Location
		bo_name_label.grid(row = 4, column = 0, sticky = "w")

		return
	elif clicked.get() == query_options[12]:
		# Part 2 - Query 10 - List Borrowers In Branch Who Borrowed A Book
		query_select_label.config(text = "List All Borrowers In A Branch Who Borrowed At Least One Book")

		# Textbox Fields Locations
		lb_branch_name_entry.grid(row = 4, column = 1)
		# Textbox Labels Location
		lb_branch_name_label.grid(row = 4, column = 0, sticky = "w")
		
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
	elif clicked.get() == query_options[17]:	# Part 3 - Query 3
		# Part 3 - Query 3 - View All Details About A Book Loan
		query_select_label.config(text = "View All Details About A Book Loan")

		# Textbox Fields Locations
		b_title_entry.grid(row = 4, column = 1)

		# Textbox Labels Location
		b_title_label.grid(row = 4, column = 0, sticky = "w")
		
		
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
# Part 2 - Query 1 Creator: Chime Nguyen
def part2_query1(query_runner):
	# Verify that any of the data being inserted into is not empty or invalid
	verified = True
	invalid_message = "The following information is missing/invalid: "

	verify_name = bo_name_entry.get()
	if not verify_name:
		verified = False
		invalid_message += "Borrower's Name. "
	verify_address = bo_address_entry.get()
	if not verify_address:
		verified = False
		invalid_message += "Borrower's Address. "
	verify_phone = bo_phone_entry.get()
	if not verify_phone:
		verified = False
		invalid_message += "Borrower's Phone. "
	if len(verify_phone) > PHONE_LENGTH:
		verified = False
		invalid_message += "Borrower's Phone Is Too Long. "

	# Return if the inputs are not valid
	if not verified:
		return invalid_message

	# Insert the filled in data into the database after verifying that the data is valid
	query_runner.execute("INSERT INTO BORROWER (Name, Address, Phone) VALUES (:name, :address, :phone)",
					  {
						  'name': verify_name,
						  'address': verify_address,
						  'phone': verify_phone
					  })
	
	# Find said user with exact details to find thei card number
	query_runner.execute("""SELECT Card_no FROM BORROWER
					  WHERE Name = ? AND Address = ? AND Phone = ?""",
					  (verify_name, verify_address, verify_phone))
	result_card_no = query_runner.fetchone()[0]

	# Clear all entries that were used
	bo_name_entry.delete(0, END)
	bo_address_entry.delete(0, END)
	bo_phone_entry.delete(0, END)
	
	result = "Inserted " + verify_name + " with Card Number " + str(result_card_no) + "."

	# Return a message that the query was successfully inserted into the table.
	return result

# Part 2 - Query 2 Creator: Chime Nguyen
def part2_query2(query_runner):
	# Verify that any of the data being inserted into is not empty or invalid
	verified = True
	invalid_message = "The following information is missing/invalid: "
	verify_entry = bo_phone_entry.get()
	if not verify_entry:
		verified = False
		invalid_message += "Updated Borrower's Phone. "
	if len(verify_entry) > PHONE_LENGTH:
		verified = False
		invalid_message += "Borrower's Phone Is Too Long. "
	verify_entry = bo_name_entry.get()
	if not verify_entry:
		verified = False
		invalid_message != "Borrower's Name. "

	# Return if the inputs are not valid
	if not verified:
		return invalid_message
	
	# Insert the filled in data into the database after verifying that the data is valid
	query_runner.execute("UPDATE BORROWER SET Phone = (:phone) WHERE Name = (:name)",
					  {
						  'phone': bo_phone_entry.get(),
						  'name': bo_name_entry.get()
					  })

	# Return a message that the query was successfully inserted into the table.
	result = "Successfully updated " + bo_name_entry.get() + "'s phone number to " + bo_phone_entry.get() + "."

	# Clear all entries that were used
	bo_name_entry.delete(0, END)
	bo_phone_entry.delete(0, END)

	# Return the result
	return result

# Part 2 - Query 3 Creator: Trung Nguyen
def part2_query3(query_runner):
	# Get input values
	branch_id_or_name = bc_branch_id_entry.get()
	num_copies = bc_no_of_copies_entry.get()

	# Check if the values are valid 
	if not branch_id_or_name or not num_copies:
		return "Please fill in all fields."
	try:
		num_copies = int(num_copies)
	except ValueError:
		return "Number of copies must be an integer."
	
	# Check if branch_id_or_name is a number or a string
	try:
		branch_id = int(branch_id_or_name)
	except ValueError:
		# If it's not an int, assume it's a branch name
		query_runner.execute("SELECT Branch_Id FROM LIBRARY_BRANCH WHERE Branch_Name = ?", (branch_id_or_name,))
		branch_id_result = query_runner.fetchone()
		if branch_id_result:
			branch_id = branch_id_result[0]
		else:
			return "Branch not found."
	else:
		branch_id = branch_id_or_name

	# Update the BOOK_COPIES table
	query_runner.execute("UPDATE BOOK_COPIES SET No_Of_Copies = No_Of_Copies + ? WHERE Branch_Id = ?", (num_copies, branch_id))
	
	# Clear the entries
	bc_branch_id_entry.delete(0, END)
	bc_no_of_copies_entry.delete(0, END)

	return "Successfully updated book copies."

# Part 2 - Query 4a Creator: Trung Nguyen
def part2_query4a(query_runner):
	# Get input values
	book_title = b_title_entry.get()
	publisher_name = b_publisher_name_entry.get()
	author_name = ba_author_name_entry.get()

	# Check if the values are valid
	if not book_title or not publisher_name or not author_name:
		results_label.config(text = "Please fill in all fields.")
		results_label.grid(row = 100, column = 0, columnspan = 2)
		return
	
	# Insert Publisher if it doesn't exist in the database
	query_runner.execute("INSERT OR IGNORE INTO PUBLISHER (Publisher_Name) VALUES (?)", (publisher_name,))

	# Insert Book
	query_runner.execute("INSERT INTO BOOK (Title, Publisher_name) VALUES (?, ?)", (book_title, publisher_name))

	# Get the Book_Id of the book that was just inserted
	query_runner.execute("SELECT Book_Id FROM BOOK WHERE Title = ? AND Publisher_name = ?", (book_title, publisher_name))
	book_id = query_runner.fetchone()[0]

	# Insert Author
	query_runner.execute("INSERT INTO BOOK_AUTHORS (Book_Id, Author_Name) VALUES (?, ?)", (book_id, author_name))

	# Clear the entries
	b_title_entry.delete(0, END)
	b_publisher_name_entry.delete(0, END)
	ba_author_name_entry.delete(0, END)

	results_label.config(text = "Successfully added new book.")
	results_label.grid(row = 100, column = 0, columnspan = 2)

	return

# Part 2 - Query 4b Creator: Trung Nguyen
def part2_query4b(query_runner):
	# Get input values
	branch_name = lb_branch_name_entry.get()
	branch_address = lb_branch_address_entry.get()

	# Check if the values are valid
	if not branch_name or not branch_address:
		results_label.config(text = "Please fill in all fields.")
		results_label.grid(row = 100, column = 0, columnspan = 2)
		return
	
	# Insert new Branch
	query_runner.execute("INSERT INTO LIBRARY_BRANCH (Branch_Name, Branch_Address) VALUES (?, ?)", (branch_name, branch_address))

	# Clear the entries
	lb_branch_name_entry.delete(0, END)
	lb_branch_address_entry.delete(0, END)

	results_label.config(text = "Successfully added new branch.")
	results_label.grid(row = 100, column = 0, columnspan = 2)

	return

# Part 2 - Query 5 Creator: Trung Nguyen
def part2_query5(query_runner):
	start_date = bl_date_out_start_entry.get()
	end_date = bl_date_out_end_entry.get()

	if not start_date or not end_date:
		results_label.config(text = "Please fill in all fields.")
		results_label.grid(row = 100, column = 0, columnspan = 2)
		return
	
	# Clear previous results
	for widget in results_frame.grid_slaves():
		widget.grid_forget() # Removes all widgets from the grid from the last query
	
	# Execute the query
	query_runner.execute("""
		SELECT B.Title, LB.Branch_Name,
			CASE WHEN BL.Returned_date IS NOT NULL THEN
				CAST(JULIANDAY(BL.Returned_date) - JULIANDAY(BL.Date_Out) AS INTEGER)
				ELSE CAST(JULIANDAY(CURRENT_DATE) - JULIANDAY(BL.Date_Out) AS INTEGER) -- Today's date meaning it was never returned
			END AS Days_Borrowed
		FROM BOOK_LOANS BL JOIN BOOK B ON BL.Book_Id = B.Book_Id
			JOIN LIBRARY_BRANCH LB ON BL.Branch_Id = LB.Branch_Id
		WHERE BL.Date_Out BETWEEN ? AND ?
		ORDER BY B.Title, LB.Branch_Name;
		""", (start_date, end_date))
	
	# Get the results
	results = query_runner.fetchall()

	# Display the results
	title = ''
	branch_name = ''
	days_borrowed = ''
	result_title = Label(results_frame, text = "Title\n______________________")
	result_branch_name = Label(results_frame, text = "Branch Name\n______________________")
	result_days_borrowed = Label(results_frame, text = "Days Borrowed\n______________________")
	for row in results:
		# Handle None values for Days_Borrowed since we have two NULL returns
		if row[2] is None:
			days_borrowed_str = str("Not Returned")
		else:
			days_borrowed_str = str(row[2])

		title += str(row[0] + "\n")
		branch_name += str(row[1] + "\n")
		days_borrowed += days_borrowed_str + "\n"

	

	# Create labels for each array of
	result_label1 = Label(results_frame, text = title)
	result_label2 = Label(results_frame, text = branch_name)
	result_label3 = Label(results_frame, text = days_borrowed)	
	# results_label.config(text = result_text)
	# results_label.grid(row = 100, column = 0, columnspan = 2)

	# Display the results using the grid and differing columns
	result_title.grid(row = 99, column = 0)
	result_branch_name.grid(row = 99, column = 1)
	result_days_borrowed.grid(row = 99, column = 2)
	result_label1.grid(row = 100, column = 0)
	result_label2.grid(row = 100, column = 1)
	result_label3.grid(row = 100, column = 2)

	# Clear the entries
	bl_date_out_start_entry.delete(0, END)
	bl_date_out_end_entry.delete(0, END)

	return

# Part 2 - Query 6 Creator: Chime Nguyen
def part2_query6(query_runner):
	# Verify that any of the data being inserted into is not empty or invalid
	verified = True
	invalid_message = "The following information is missing/invalid: "
	verify_entry = bl_returned_date_entry.get()
	if not verify_entry:
		verified = False
		invalid_message += "Return Date. "

	# Return if the inputs are not valid
	if not verified:
		return invalid_message
	
	# Select borrower's name based on when they returned their book
	query_runner.execute("""SELECT DISTINCT bo.Name AS Borrower_Names
					  FROM BORROWER bo JOIN BOOK_LOANS bl ON bo.Card_No = bl.Card_No
					  WHERE Returned_date = (:return_date)""",
					  {
						  'return_date': bl_returned_date_entry.get()
					  })
	
	records = query_runner.fetchall()

	print(records)

	results = ''

	for record in records:
		results += str(record[0] + "\n")
	
	return results

# Part 2 - Query 7 Creator: Chime Nguyen
def part2_query7(query_runner):
	# Count the number of books from all branches, including returned, currently borrowed, and late books
	query_runner.execute("""SELECT lb.Branch_Name, COUNT(*) AS Book_Count,
					  COUNT(CASE WHEN bl.Returned_date IS NOT 'NULL' THEN 1 END) AS Returned_Books, 
					  COUNT(CASE WHEN bl.Returned_date IS 'NULL' THEN 1 END) AS Still_Borrowed_Books, 
					  COUNT(CASE WHEN bl.Returned_date IS NOT 'NULL' AND bl.Returned_date > bl.Due_Date THEN 1 END) AS Late_Books
					  FROM LIBRARY_BRANCH lb JOIN BOOK_LOANS bl ON lb.Branch_Id = bl.Branch_Id
					  GROUP BY lb.Branch_Name
					  """)
	
	# Fetch the query results and store it into a variable
	records = query_runner.fetchall()

	# For debugging purposes, print all of the records into the terminal
	# print(records)

	# Names to store string representation of data
	result_branch_name = ''
	result_book_count = ''
	result_returned_books = ''
	result_still_borrowed_books = ''
	result_late_books = ''

	# Store each data into a particular string array for displaying into the GUI
	for record in records:
		result_branch_name += str(record[0] + "\n")
		result_book_count += str(str(record[1]) + "\n")
		result_returned_books += str(str(record[2]) + "\n")
		result_still_borrowed_books += str(str(record[3]) + "\n")
		result_late_books += str(str(record[4]) + "\n")

	# For debugging purposes, print each string array into the terminal one at a time
	# print(result_branch_name)
	# print()
	# print(result_book_count)
	# print()
	# print(result_returned_books)
	# print()
	# print(result_still_borrowed_books)
	# print()
	# print(result_late_books)
	# print()
	
	# Return all string arrays back to do_query function to display the grid properly
	return (result_branch_name, result_book_count, result_returned_books,
		 result_still_borrowed_books, result_late_books)

# Part 2 - Query 8 Creator: Chime Nguyen
def part2_query8(query_runner):
	# List all of the book titles with the maximum number of days that the book has been borrowed for.
	query_runner.execute("""SELECT b.Title, MAX(CASE WHEN bl.Returned_date = 'NULL' THEN NULL 
					  ELSE CAST(JULIANDAY(bl.Returned_date) - JULIANDAY(bl.Date_Out) AS INTEGER) END) AS Days_borrowed 
					  FROM BOOK b JOIN BOOK_LOANS bl ON b.Book_Id = bl.Book_Id 
					  GROUP BY b.Book_Id 
					  ORDER BY Days_borrowed DESC
					  """)
	
	# Fetch the query results and store it into a variable
	records = query_runner.fetchall()

	# For debugging purposes, print all of the records into the terminal
	# print(records)

	# Names to store string representation of data
	result_book_title = ''
	result_max_days_borrowed = ''

	# Store each data into a particular string array for displaying into the GUI
	for record in records:
		result_book_title += str(record[0] + "\n")
		result_max_days_borrowed += str(str(record[1]) + "\n")

	# For debugging purposes, print each string array into the terminal one at a time
	# print(result_book_title)
	# print()
	# print(result_max_days_borrowed)
	# print()

	# Return all string arrays back to do_query function to display the grid properly
	return (result_book_title, result_max_days_borrowed)

# Part 2 - Query 9 Creator: Ivan
def part2_query9(query_runner):
	verified = True
	invalid_message = "The following information is missing/invalid: "
	verify_entry = bo_name_entry.get()
	if not verify_entry:
		verified = False
		invalid_message += "Borrower's Name. "

	if not verified:
		return invalid_message
	
	query_runner.execute("""
						SELECT bo.Name, b.Title, ba.Author_Name AS Author, bl.Date_Out, 
    						CASE WHEN bl.Returned_date IS NOT 'NULL' THEN
        						CAST(JULIANDAY(bl.Returned_date) - JULIANDAY(bl.Date_Out) AS INTEGER)
        						ELSE 'NULL'
    						END AS Days_borrowed,
    						CASE
        						WHEN bl.Returned_date IS 'NULL' THEN 'Not Returned'
        						WHEN bl.Returned_date IS NOT 'NULL' AND JULIANDAY(bl.Returned_date) > JULIANDAY(bl.Due_Date)
        						THEN 'Late' ELSE 'On Time'
    						END AS Return_Status
						FROM BOOK b JOIN BOOK_LOANS bl ON b.Book_Id = bl.Book_Id
            						JOIN BORROWER bo ON bl.Card_No = bo.Card_No
            						JOIN BOOK_AUTHORS ba ON b.Book_Id = ba.Book_Id
						WHERE bo.Name = (:name)
						ORDER BY Date_Out DESC;
						""", {'name': bo_name_entry.get()})
	
	records = query_runner.fetchall()
	print(records)



	return "Successfully executed query 9"

# Part 2 - Query 10 Creator: Ivan
def part2_query10(query_runner):
	verified = True
	invalid_message = "The following information is missing/invalid: "
	verify_entry = lb_branch_name_entry.get()
	if not verify_entry:
		verified = False
		invalid_message += "Branch name. "

	if not verified:
		return invalid_message
	
	query_runner.execute("""
						SELECT DISTINCT bo.Name, bo.Address, lb.Branch_Name
						FROM BORROWER bo JOIN BOOK_LOANS bl ON bo.Card_No = bl.Card_No
                 						 JOIN LIBRARY_BRANCH lb ON bl.Branch_Id = lb.Branch_Id
						WHERE lb.Branch_Name = (:branch_name);
					  	""", {'branch_name': lb_branch_name_entry.get()})
	
	records = query_runner.fetchall()
	print(records)



	return "Successfully executed query 10"

# Part 3 - Query 1 Creator: Ivan
def part3_query1():
	query_conn = sqlite3.connect('test.db')
	query_runner = query_conn.cursor()

	query_runner.execute("ALTER TABLE BOOK_LOANS ADD COLUMN Late INTEGER;")
	query_runner.execute("""
						UPDATE BOOK_LOANS
						SET Late = (
    						CASE
        						WHEN CAST(JULIANDAY(Returned_date) > JULIANDAY(Due_Date) AS INTEGER) THEN 1
        						WHEN CAST(JULIANDAY(Returned_date) <= JULIANDAY(Due_Date) AS INTEGER) THEN 0
        						ELSE 0
    						END
    						);
					  	""")
	
	query_conn.commit()
	query_conn.close()

	return "Successfully executed query 3.1"

# Part 3 - Query 2 Creator: Ivan
def part3_query2():
	query_conn = sqlite3.connect('test.db')
	query_runner = query_conn.cursor()

	query_runner.execute("ALTER TABLE LIBRARY_BRANCH ADD COLUMN LateFee FLOAT DEFAULT 0.00;")
	query_runner.execute("""
						UPDATE LIBRARY_BRANCH
						SET LateFee = (
    						CASE
        						WHEN Branch_Name = 'Main Branch' THEN 100.00
        						WHEN Branch_Name = 'West Branch' THEN 50.00
        						WHEN Branch_Name = 'East Branch' THEN 10.00
        						ELSE 420.69
    						END
    						);
					  	""")

	query_conn.commit()
	query_conn.close()

	return "Successfully executed query 3.2"

# Part 3 - Query 3 Creator: Trung Nguyen
def part3_query3(query_runner):
	# Drop the view if it exists already
	query_runner.execute("DROP VIEW IF EXISTS vBookLoanInfo;")

	query_runner.execute("""
		CREATE VIEW vBookLoanInfo AS
		SELECT
			BL.Card_No,
			BR.Name AS 'Borrower Name',
			BL.Date_Out,
			BL.Due_Date,
			BL.Returned_date,		  
			CAST((JULIANDAY(BL.Returned_date) - JULIANDAY(BL.Date_Out)) AS INTEGER) AS 'TotalDays',
			B.Title AS 'Book Title',
			CASE WHEN BL.Late = 1
				THEN CAST((JULIANDAY(BL.Returned_date) - JULIANDAY(BL.Due_Date)) AS INTEGER)
				ELSE 0
			END AS 'DaysLate',
			BL.Branch_Id,
			CASE WHEN BL.Late = 1
				THEN CAST((JULIANDAY(BL.Returned_date) - JULIANDAY(BL.Due_Date)) AS INTEGER) * LB.LateFee
				ELSE 0
			END AS 'LateFeeBalance'
		FROM BOOK_LOANS BL
		JOIN BORROWER BR ON BL.Card_No = BR.Card_No
		JOIN BOOK B ON BL.Book_Id = B.Book_Id
		JOIN LIBRARY_BRANCH LB ON BL.Branch_Id = LB.Branch_Id;
		""")
	
	# Query the view for the specific book title 
	print(b_title_entry.get())
	query_runner.execute("SELECT * FROM vBookLoanInfo WHERE \"Book Title\" = ?", (b_title_entry.get(),))
	
	# Get the results
	results = query_runner.fetchall()

	# Clear the old results from the frame 
	for widget in results_frame.grid_slaves():
		widget.grid_forget() # Removes all widgets from the grid from the last query
	
	# Display the results
	if results:
		# Define headers for the table
		headers = ["Card No", 
			"Borrower Name", 
			"Date Out", 
			"Due Date", 
			"Returned Date", 
			"Total Days", 
			"Book Title", 
			"Days Late", 
			"Branch Id", 
			"Late Fee Balance"]

		# Display headers in the first row
		# There's 10 columns from the headers
		for col in range(len(headers)):
			header_label = Label(results_frame, text=headers[col])
			header_label.grid(row=0, column=col)

		# Display each row of results
		for row_index in range(len(results)):
			# Get the current row data
			current_row = results[row_index]

			# Display each value in the current row
			for col_index in range(len(current_row)):
				value = current_row[col_index]
				result_label = Label(results_frame, text=value)
				result_label.grid(row=row_index + 1, column=col_index)
	else:
		# If no results found
		book_title = b_title_entry.get()
		no_results_label = Label(results_frame, text=f"No results found for: {book_title}")
		no_results_label.grid(row=1, column=0)

	# Clear the entries
	b_title_entry.delete(0, END)


	return

	
# END ==================================== Query  Functions ==================================== END



# This stuff should NOT be changed
# BEGIN ============================== Complete Queries Command ============================== BEGIN
# General Do Query Creator: Chime Nguyen
def do_query():
	# Create a new connection dedicated to the queries
	query_conn = sqlite3.connect('LMS_2.db') # Edit this to be the right database name

	# Remove previous results details
	for widget in results_frame.grid_slaves():
		widget.grid_forget()
	
	# Use this cursor to run the query
	query_runner = query_conn.cursor()

	# Create a frame for the results based on query
	if clicked.get() == query_options[2]:
		# Do computations for Part 2 - Query 1
		results_text = part2_query1(query_runner)
		results_label.config(text = results_text)

	elif clicked.get() == query_options[3]:
		# Do computations for Part 2 - Query 2
		results_text = part2_query2(query_runner)
		results_label.config(text = results_text)

	elif clicked.get() == query_options[4]:
		# Do computations for Part 2 - Query 3
		results_text = part2_query3(query_runner)
		results_label.config(text = results_text)

	elif clicked.get() == query_options[5]:
		# Do computations for Part 2 - Query 4a
		results_text = part2_query4a(query_runner)
		results_label.config(text = results_text)

	elif clicked.get() == query_options[6]:
		# Do computations for Part 2 - Query 4b
		results_text = part2_query4b(query_runner)
		results_label.config(text = results_text)

	elif clicked.get() == query_options[7]:
		# Do computations for Part 2 - Query 5
		results_text = part2_query5(query_runner)
		results_label.config(text = results_text)

	elif clicked.get() == query_options[8]:
		# Do computations for Part 2 - Query 6
		results_text = part2_query6(query_runner)
		results_label.config(text = results_text)

	elif clicked.get() == query_options[9]:
		# Do computations for Part 2 - Query 7
		(result_branch_name, result_book_count, result_returned_books,
		 result_still_borrowed_books, result_late_books) = part2_query7(query_runner)
		
		# Create seperate labels for displaying results separately
		results0a = Label(results_frame, text = "Branch Name", justify = "left")
		results0b = Label(results_frame, text = "Book Count", justify = "left")
		results0c = Label(results_frame, text = "Returned Books", justify = "left")
		results0d = Label(results_frame, text = "Still Borrowed Books", justify = "left")
		results0e = Label(results_frame, text = "Late Books", justify = "left")

		results1 = Label(results_frame, text = result_branch_name, justify = "left")
		results2 = Label(results_frame, text = result_book_count, justify = "left")
		results3 = Label(results_frame, text = result_returned_books, justify = "left")
		results4 = Label(results_frame, text = result_still_borrowed_books, justify = "left")
		results5 = Label(results_frame, text = result_late_books, justify = "left")

		# Add the results of the query into the grid and display them properly
		results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 2)
		results0b.grid(row = RESULTS_ROW-1, column = 1, padx = 2)
		results0c.grid(row = RESULTS_ROW-1, column = 2, padx = 2)
		results0d.grid(row = RESULTS_ROW-1, column = 3, padx = 2)
		results0e.grid(row = RESULTS_ROW-1, column = 4, padx = 2)

		results1.grid(row = RESULTS_ROW, column = 0, padx = 2, sticky = "w")
		results2.grid(row = RESULTS_ROW, column = 1, padx = 2, sticky = "w")
		results3.grid(row = RESULTS_ROW, column = 2, padx = 2, sticky = "w")
		results4.grid(row = RESULTS_ROW, column = 3, padx = 2, sticky = "w")
		results5.grid(row = RESULTS_ROW, column = 4, padx = 2, sticky = "w")

	elif clicked.get() == query_options[10]:
		# Do computations for Part 2 - Query 8
		(result_book_title, result_max_days_borrowed) = part2_query8(query_runner)

		# Create seperate labels for displaying results separately
		results0a = Label(results_frame, text = "Book Title", justify = "left")
		results0b = Label(results_frame, text = "Max Days Borrowed", justify = "left")

		results1 = Label(results_frame, text = result_book_title, justify = "left")
		results2 = Label(results_frame, text = result_max_days_borrowed, justify = "left")

		# Add the results of the query into the grid and display them properly
		results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 22, sticky = "w")
		results0b.grid(row = RESULTS_ROW-1, column = 1, padx = 22, sticky = "w")

		results1.grid(row = RESULTS_ROW, column = 0, padx = 22, sticky = "w")
		results2.grid(row = RESULTS_ROW, column = 1, padx = 22, sticky = "w")


	elif clicked.get() == query_options[11]:
		# Do computations for Part 2 - Query 9
		results_text = part2_query9(query_runner)
		results_label.config(text = results_text)

	elif clicked.get() == query_options[12]:
		# Do computations for Part 2 - Query 10
		results_text = part2_query10(query_runner)
		results_label.config(text = results_text)

	elif clicked.get() == query_options[15]:
		# Do computations for Part 3 - Query 1
		results_text = part3_query1()
		results_label.config(text = results_text)

	elif clicked.get() == query_options[16]:
		# Do computations for Part 3 - Query 2
		results_text = part3_query2()
		results_label.config(text = results_text)

	elif clicked.get() == query_options[17]:
		# Do computations for Part 3 - Query 3
		results_text = part3_query3(query_runner)
		results_label.config(text = results_text)

	else:
		results_label.config(text = "")

	results_label.grid(row = RESULTS_ROW, column = 0, columnspan = MAX_COLUMNSPAN)

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
	conn = sqlite3.connect('LMS_2.db') # Edit this to be the right database name

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



# BEGIN ==================================== Import Datas ==================================== BEGIN
def import_csv_files():
    dataset_dir = "LMSDataset"
    csv_files = [f for f in os.listdir(dataset_dir) if f.endswith('.csv')]
    
    for csv_file in csv_files:
        table_name = os.path.splitext(csv_file)[0].upper()
        file_path = os.path.join(dataset_dir, csv_file)
        
        conn = sqlite3.connect('LMS_2.db') # Edit this to be the right database name
        cursor = conn.cursor()
        
        with open(file_path, 'r') as file: # Open file for reading
            csv_reader = csv.reader(file) 
            headers = next(csv_reader) # First row is header 
            
            # Get the table structure
			# PRAGMA gets the list of tuples and information and store into the cursor
            cursor.execute(f"PRAGMA table_info({table_name})")
			# PRAGMA returns: cid, name, type, notnull, dflt_value, pk
			# fetchall gets the rows returned by PRAGMA above
			# get the column name from the second element (name) of the tuple
            table_columns = [column[1] for column in cursor.fetchall()]
            
            # Prepare the INSERT statement
            columns = ', '.join(table_columns)
			# Placeholders to make sure you have the correct number of columns
			# The number of placeholders should match the number of columns
			# Should look like this (?, ?, ?, ...)
            placeholders = ', '.join(['?' for _ in table_columns])
			# This is just sqlite3 syntax for inserting data into a table
            insert_query = f"INSERT OR REPLACE INTO {table_name} ({columns}) VALUES ({placeholders})"
            
            # Insert data
            for row in csv_reader:
                # Make sure the row has the correct number of elements
                if len(row) != len(table_columns):
                    print(f"Skipping row in {csv_file}: {row}")
                    continue
                
                cursor.execute(insert_query, row)
        
        conn.commit()
        conn.close()
    
    print("CSV files imported successfully")

# Import CSV files
import_csv_files()
# END ====================================== Import Datas ====================================== END



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
query_select_label.grid(row = 2, column = 0, columnspan = MAX_COLUMNSPAN)

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
p_publisher_name_label = Label(textfield_frame, text = "Publisher's Name", width = 30)
p_phone_label = Label(textfield_frame, text = "Publisher's Phone", width = 30)
p_address_label = Label(textfield_frame, text = "Publisher's Address", width = 30)

# These are all of the labels for the attributes from the LIBRARY_BRANCH table
# Not all attributes may be used here
lb_branch_id_label = Label(textfield_frame, text = "Library Branch ID", width = 30)
lb_branch_name_label = Label(textfield_frame, text = "Library Branch's Name", width = 30)
lb_branch_address_label = Label(textfield_frame, text = "Library Branch's Address", width = 30)

# These are all of the labels for the attributes from the BORROWER table
# Not all attributes may be used here
bo_name_label = Label(textfield_frame, text = "Borrower's Name", width = 30)
bo_address_label = Label(textfield_frame, text = "Borrower's Address", width = 30)
bo_phone_label = Label(textfield_frame, text = "Borrower's Phone", width = 30)

# These are all of the labels for the attributes from the BOOK table
# Not all attributes may be used here
b_book_id_label = Label(textfield_frame, text = "Book ID", width = 30)
b_title_label = Label(textfield_frame, text = "Book Title", width = 30)
b_publisher_name_label = Label(textfield_frame, text = "Book Publisher's Name", width = 30)

# These are all of the labels for the attributes from the BOOK_LOANS table
# Not all attributes may be used here
bl_book_id_label = Label(textfield_frame, text = "Book ID", width = 30)
bl_branch_id_label = Label(textfield_frame, text = "Library Branch ID", width = 30)
bl_card_no_label = Label(textfield_frame, text = "Borrower Card No", width = 30)
bl_date_out_label = Label(textfield_frame, text = "Date Out", width = 30)
bl_due_date_label = Label(textfield_frame, text = "Due Date", width = 30)
bl_returned_date_label = Label(textfield_frame, text = "Return Date", width = 30)

# These are all of the labels for the attributes from the BOOK_COPIES table
# Not all attributes may be used here
bc_book_id_label = Label(textfield_frame, text = "Book ID", width = 30)
bc_branch_id_label = Label(textfield_frame, text = "Library Branch ID", width = 30)
bc_no_of_copies_label = Label(textfield_frame, text = "Number Of Copies", width = 30)

# These are all of the labels for the attributes from the BOOK_AUTHORS table
# Not all attributes may be used here
ba_book_id_label = Label(textfield_frame, text = "Book ID", width = 30)
ba_author_name_label = Label(textfield_frame, text = "Author's Name", width = 30)
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
bl_date_out_start_entry = Entry(textfield_frame, width = 30)
bl_date_out_end_entry = Entry(textfield_frame, width = 30)


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