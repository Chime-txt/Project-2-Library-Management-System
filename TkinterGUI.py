# Install GUI For Python
# -- PyQt5 : pip3 install PyQt5
# -- Tkinter: pip3 install tkinter
# -- Kivy: pip3 install kivy

# Import TKinter
from tkinter import *
import sqlite3
import csv
import os
import random

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
root.geometry("800x800")
root.minsize(800, 800)
root.maxsize(800, 100)
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
	"Reset Database",					# query_options[20]
	"======= Testing stuff ========",	# query_options[21]
	"Check out a Book",					# query_options[22]
	"Sign up a new Borrower",			# query_options[23]
	"Add new Book to All Branches",		# query_options[24]
	"Check copies Loaned",				# query_options[25]
	"Check for Late Returns",			# query_options[26]
	"Generalized Info of Book Loans",	# query_options[27]
	"View Book Loan via Borrower",		# query_options[28]
	"View Book Loan via Book"			# query_options[29]

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
		query_select_label.config(text = "Create A Report On A Borrower With All Of Their Book Loan Details")

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
		lb_branch_name_entry.grid(row = 4, column = 1)
		lb_branch_latefee_entry.grid(row = 5, column = 1)
		# Textbox Labels Location
		# lb_branch_name_label = Label(textfield_frame, text = "Library Branch Name:") # Already created so this is causing issues
		lb_branch_name_label.grid(row = 4, column = 0, sticky = "w")
		# lb_branch_latefee_label = Label(textfield_frame, text = "Library Branch Late Fee:")
		lb_branch_latefee_label.grid(row =5, column = 0, sticky = "w")

		return
	elif clicked.get() == query_options[17]:	# Part 3 - Query 3
		# Part 3 - Query 3 - View All Details About A Book Loan
		query_select_label.config(text = "View All Details About A Book Loan")

		# Textbox Fields Locations
		b_title_entry.grid(row = 4, column = 1)

		# Textbox Labels Location
		b_title_label.grid(row = 4, column = 0, sticky = "w")
		
		
		return
	#########################TESTING REQUIREMENTS STUFF ####################################
	elif clicked.get() == query_options[22]: 	# Check out a Book (Requirement 1)
		# Part 3 - Requirement 1 - Check out a book, add to Book_Loan, 
		# the number of copies needs to be updated via trigger in Book_copies table
		# Show output of updated Book_Copies table [10 points]
		query_select_label.config(text = "Check out a Book")

		# Textbox Fields Locations
		bl_card_no_entry.grid(row = 4, column = 1)
		bc_branch_id_entry.grid(row = 5, column = 1)
		b_book_id_entry.grid(row = 6, column = 1)

		# Textbox Labels Location
		bl_card_no_label.grid(row = 4, column = 0, sticky = "w")
		branch_name_or_id_label = Label(textfield_frame, text = "Library Branch's Name or ID", width = 30)
		branch_name_or_id_label.grid(row = 5, column = 0, sticky = "w")
		book_id_or_title_label = Label(textfield_frame, text = "Book ID or Title", width = 30)
		book_id_or_title_label.grid(row = 6, column = 0, sticky = "w")


		return
	elif clicked.get() == query_options[23]: 	# Sign up a new Borrower (Requirement 2)
		# Part 3 - Requirement 2 - Add information about new Borrower. Do not provide CardNo in query.
		# Output the card number as if you are giving a new library card. [3 points]
		query_select_label.config(text = "Sign up a new Borrower")

		# Textbox Fields Locations
		bo_name_entry.grid(row = 4, column = 1)
		bo_address_entry.grid(row = 5, column = 1)
		bo_phone_entry.grid(row = 6, column = 1)

		# Textbox Labels Location
		# bo_name_label = Label(textfield_frame, text = "New Borrower's Name") # Already created so this is causing issues 
		bo_name_label.grid(row = 4, column = 0, sticky = "w")
		# bo_address_label = Label(textfield_frame, text = "Borrower's Address") # Already created so this is causing issues
		bo_address_label.grid(row = 5, column = 0, sticky = "w")
		# bo_phone_label = Label(textfield_frame, text = "Borrower's Phone Number") # Already created so this is causing issues
		bo_phone_label.grid(row = 6, column = 0, sticky = "w")
		

		return
	elif clicked.get() == query_options[24]: 	# Add new Book to All Branches (Requirement 3)
		# Part 3 - Requirement 3 - Add a new book with publisher (you can use a publisher that already exists) 
		# and author information to all 5 branches with 5 copies for each branch. [5 points]
		query_select_label.config(text = "Add new Book to All Branches")

		# Textbox Fields Locations
		b_title_entry.grid(row = 4, column = 1)
		ba_author_name_entry.grid(row = 5, column = 1)
		b_publisher_name_entry.grid(row = 6, column = 1)

		# Textbox Labels Location
		b_title_label.grid(row = 4, column = 0, sticky = "w")
		ba_author_name_label.grid(row = 5, column = 0, sticky = "w")
		b_publisher_name_label.grid(row = 6, column = 0, sticky = "w")

		return
	elif clicked.get() == query_options[25]: 	# Check copies Loaned (Requirement 4)
		# Part 3 - Requirement 4 - Given a book title list the number of copies loaned out per branch. [5 points]
		query_select_label.config(text = "Check copies Loaned")

		# Textbox Fields Locations
		b_title_entry.grid(row = 4, column = 1)

		# Textbox Labels Location
		b_title_label.grid(row = 4, column = 0, sticky = "w")

		return
	elif clicked.get() == query_options[26]: 	# Check for Late Returns (Requirement 5)
		# Part 3 - Requirement 5 - Given any due date range list the Book_loans that were returned late 
		# and how many days they were late [8 points]
		query_select_label.config(text = "Check for Late Returns")
		
		# Textbox Fields Locations
		bl_date_out_start_entry.grid(row = 4, column = 1)
		bl_date_out_end_entry.grid(row = 5, column = 1)

		# Textbox Labels Location
		bl_date_out_start_label = Label(textfield_frame, text = "Start Date (YYYY-MM-DD)")
		bl_date_out_start_label.grid(row = 4, column = 0, sticky = "w")
	
		bl_date_out_end_label = Label(textfield_frame, text = "End Date (YYYY-MM-DD)")
		bl_date_out_end_label.grid(row = 5, column = 0, sticky = "w")

		return
	elif clicked.get() == query_options[27]: 	# View Info on a Book Loan (Requirement 6)
		# Part 3 - Requirement 6 - return view's results by applying criteria
		# List for every borrower the ID, name, and if there is any lateFee balance.
		# The user has the right to search either by a borrower ID, name, part of the name or run query with no filters/criteria.
		# Amount needs to be in US dollars. For borrrowers with zero(0) or NULL balanace, you need to return zero dollars ($0.00)
		# Make sure that the query returns meaningful attribute names.
		# In the case that the user decides not to provide any filters, order the results based on balance amount. 
		# Make sure you return all records 
		### idk if this is a part two but here it is: ###
		# List book information in the view. user must search with borrowerID and any of the following search items:
		# book id, book title, part of book title, or run query with no filters/criteria
		# The late fee amount needs to be in US dollars. The late fee price amount needs to have two decimals as well as $ sign
		# For books that they do not have any late fee amount, you need to substitute NULL value with 'Non-Appliable' text
		# Make sure that the query returns meaningful attribute names
		# In the case that the user decides not to provide any filters, order the results based on highest late fee remaining.
		query_select_label.config(text = "View Info on a Book Loan\n You may leave entires blank.")

		# Textbox Fields Locations
		bl_card_no_entry.grid(row = 4, column = 1)
		bo_name_entry.grid(row = 5, column = 1)
		b_book_id_entry.grid(row = 6, column = 1)
		b_title_entry.grid(row = 7, column = 1)

		# Textbox Labels Location
		bl_card_no_label.grid(row = 4, column = 0, sticky = "w")
		bo_name_label.grid(row = 5, column = 0, sticky = "w")
		b_book_id_label.grid(row = 6, column = 0, sticky = "w")
		b_title_label.grid(row = 7, column = 0, sticky = "w")

		return
	
	elif clicked.get() == query_options[28]: 	# View Book Loan via Borrower (Requirement 6a)
		# List for every borrower the ID, name, and if there is any lateFee balance.
		# The user has the right to search either by a borrower ID, name, part of the name or run query with no filters/criteria.
		# Amount needs to be in US dollars. For borrrowers with zero(0) or NULL balanace, you need to return zero dollars ($0.00)
		# Make sure that the query returns meaningful attribute names.
		# In the case that the user decides not to provide any filters, order the results based on balance amount. 
		# Make sure you return all records 
		query_select_label.config(text = "View Book Loan via Borrower\n You may leave entires blank.")

		# Textbox Fields Locations
		bl_card_no_entry.grid(row = 4, column = 1)
		bo_name_entry.grid(row = 5, column = 1)

		# Textbox Labels Location
		bl_card_no_label.grid(row = 4, column = 0, sticky = "w")
		bo_name_label.grid(row = 5, column = 0, sticky = "w")
	
		return
	
	elif clicked.get() == query_options[29]: 	# View Book Loan via Book (Requirement 6b)
		# List book information in the view. user must search with borrowerID and any of the following search items:
		# book id, book title, part of book title, or run query with no filters/criteria
		# The late fee amount needs to be in US dollars. The late fee price amount needs to have two decimals as well as $ sign
		# For books that they do not have any late fee amount, you need to substitute NULL value with 'Non-Appliable' text
		# Make sure that the query returns meaningful attribute names
		# In the case that the user decides not to provide any filters, order the results based on highest late fee remaining.
		query_select_label.config(text = "View Book Loan via Book\n You may leave entires blank.")

		# Textbox Fields Locations
		bl_card_no_entry.grid(row = 4, column = 1)
		b_book_id_entry.grid(row = 5, column = 1)
		b_title_entry.grid(row = 6, column = 1)

		# Textbox Labels Location
		bl_card_no_label.grid(row = 4, column = 0, sticky = "w")
		b_book_id_label.grid(row = 5, column = 0, sticky = "w")
		b_title_label.grid(row = 6, column = 0, sticky = "w")

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
		return (invalid_message,0,0,0)

	# Insert the filled in data into the database after verifying that the data is valid
	query_runner.execute("INSERT INTO BORROWER (Name, Address, Phone) VALUES (:name, :address, :phone)",
					  {
						  'name': verify_name,
						  'address': verify_address,
						  'phone': verify_phone
					  })
	
	# Find said user with exact details to find thei card number
	query_runner.execute("SELECT * FROM BORROWER;")
	records = query_runner.fetchall()

	result_card = ''
	result_name = ''
	result_address = ''
	result_phone = ''

	for record in records:
		result_card += str(str(record[0]) + "\n")
		result_name += str(record[1] + "\n")
		result_address += str(record[2] + "\n")
		result_phone += str(record[3] + "\n")

	# Clear all entries that were used
	bo_name_entry.delete(0, END)
	bo_address_entry.delete(0, END)
	bo_phone_entry.delete(0, END)

	success_message = f"Successfully added new Borrower.\n"
	success_label = Label(results_frame, text=success_message)
	success_label.grid(row=RESULTS_ROW-2, column=0, columnspan=3)

	# Return a message that the query was successfully inserted into the table.
	return (result_card, result_name, result_address, result_phone)

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
		return (invalid_message,0,0,0)
	
	# Insert the filled in data into the database after verifying that the data is valid
	query_runner.execute("UPDATE BORROWER SET Phone = (:phone) WHERE Name = (:name)",
					  {
						  'phone': bo_phone_entry.get(),
						  'name': bo_name_entry.get()
					  })

	# Return a message that the query was successfully inserted into the table.
	query_runner.execute("SELECT * FROM BORROWER;")
	records = query_runner.fetchall()

	result_card = ''
	result_name = ''
	result_address = ''
	result_phone = ''

	for record in records:
		result_card += str(str(record[0]) + "\n")
		result_name += str(record[1] + "\n")
		result_address += str(record[2] + "\n")
		result_phone += str(record[3] + "\n")


	# Clear all entries that were used
	bo_name_entry.delete(0, END)
	bo_phone_entry.delete(0, END)

	success_message = f"Successfully updated Borrower's Phone Number.\n"
	success_label = Label(results_frame, text=success_message)
	success_label.grid(row=RESULTS_ROW-2, column=0, columnspan=3)

	# Return the result
	return (result_card, result_name, result_address, result_phone)

# Part 2 - Query 3 Creator: Trung Nguyen
def part2_query3(query_runner):
	# Get input values
	branch_id_or_name = bc_branch_id_entry.get()
	num_copies = bc_no_of_copies_entry.get()

	# Check if the values are valid 
	if not branch_id_or_name or not num_copies:
		return ("Please fill in all fields.",0,0)
	try:
		num_copies = int(num_copies)
	except ValueError:
		return ("Number of copies must be an integer.",0,0)
	
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
			return ("Branch not found.",0,0)
	else:
		branch_id = branch_id_or_name

	# Update the BOOK_COPIES table
	query_runner.execute("UPDATE BOOK_COPIES SET No_Of_Copies = No_Of_Copies + ? WHERE Branch_Id = ?", (num_copies, branch_id))
	
	query_runner.execute("SELECT * FROM BOOK_COPIES;")
	records = query_runner.fetchall()

	result_bookId = ''
	result_branchId = ''
	result_copies = ''
	
	for record in records:
		result_bookId += str(str(record[0]) + "\n")
		result_branchId += str(str(record[1]) + "\n")
		result_copies += str(str(record[2]) + "\n")


	# Clear the entries
	bc_branch_id_entry.delete(0, END)
	bc_no_of_copies_entry.delete(0, END)

	success_message = f"Successfully increased number of Book Copies.\n"
	success_label = Label(results_frame, text=success_message)
	success_label.grid(row=RESULTS_ROW-2, column=0, columnspan=3)

	return (result_bookId, result_branchId, result_copies)

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
		return (0,0,0)
	
	# Insert Publisher if it doesn't exist in the database
	query_runner.execute("INSERT OR IGNORE INTO PUBLISHER (Publisher_Name) VALUES (?)", (publisher_name,))

	# Insert Book
	query_runner.execute("INSERT INTO BOOK (Title, Publisher_name) VALUES (?, ?)", (book_title, publisher_name))

	# Get the Book_Id of the book that was just inserted
	query_runner.execute("SELECT Book_Id FROM BOOK WHERE Title = ? AND Publisher_name = ?", (book_title, publisher_name))
	book_id = query_runner.fetchone()[0]

	# Insert Author
	query_runner.execute("INSERT INTO BOOK_AUTHORS (Book_Id, Author_Name) VALUES (?, ?)", (book_id, author_name))

	# Get the results
	query_runner.execute("""
					  SELECT bo.Title, bo.Publisher_name, ba.Author_Name
					  FROM BOOK bo JOIN BOOK_AUTHORS ba ON bo.Book_Id = ba.Book_Id;
					  """)
	records = query_runner.fetchall()

	result_title = ''
	result_Pname = ''
	result_Aname = ''

	for record in records:
		result_title += str(record[0] + "\n")
		result_Pname += str(record[1] + "\n")
		result_Aname += str(record[2] + "\n")
	

	# Clear the entries
	b_title_entry.delete(0, END)
	b_publisher_name_entry.delete(0, END)
	ba_author_name_entry.delete(0, END)

	success_message = f"Successfully added new book.\n"
	success_label = Label(results_frame, text=success_message)
	success_label.grid(row=RESULTS_ROW-2, column=0, columnspan=3)

	return (result_title, result_Pname, result_Aname)

# Part 2 - Query 4b Creator: Trung Nguyen
def part2_query4b(query_runner):
	# Get input values
	branch_name = lb_branch_name_entry.get()
	branch_address = lb_branch_address_entry.get()

	# Check if the values are valid
	if not branch_name or not branch_address:
		results_label.config(text = "Please fill in all fields.")
		results_label.grid(row = 100, column = 0, columnspan = 2)
		return (0,0,0)
	
	# Insert new Branch
	query_runner.execute("INSERT INTO LIBRARY_BRANCH (Branch_Name, Branch_Address) VALUES (?, ?)", (branch_name, branch_address))

	# Get the results
	query_runner.execute("SELECT Branch_Id, Branch_Name, Branch_Address FROM LIBRARY_BRANCH;")
	records = query_runner.fetchall()

	result_branch_id = ''
	result_branch_name = ''
	result_branch_address = ''

	for record in records:
		result_branch_id += str(str(record[0]) + "\n")
		result_branch_name += str(record[1] + "\n")
		result_branch_address += str(record[2] + "\n")

	# Clear the entries
	lb_branch_name_entry.delete(0, END)
	lb_branch_address_entry.delete(0, END)

	success_message = f"Successfully added new branch.\n"
	success_label = Label(results_frame, text=success_message)
	success_label.grid(row=RESULTS_ROW-2, column=0, columnspan=3)

	return (result_branch_id, result_branch_name, result_branch_address)

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

	result_borrower_name = ''
	result_book_title = ''
	result_Author = ''
	result_Date_out = ''

	for record in records:
		result_borrower_name += str(record[0] + "\n")
		result_book_title += str(record[1] + "\n")
		result_Author += str(record[2] + "\n")
		result_Date_out += str(record[3] + "\n")

	# Clear the entries
	bo_name_entry.delete(0, END)

	return (result_borrower_name, result_book_title, result_Author, result_Date_out)

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

	result_borrower_name = ''
	result_borrower_address = ''
	result_library_branch_name = ''

	for record in records:
		result_borrower_name += str(record[0] + "\n")
		result_borrower_address += str(record[1] + "\n")
		result_library_branch_name += str(record[2] + "\n")

	# Clear the entries
	lb_branch_name_entry.delete(0, END)

	return (result_borrower_name, result_borrower_address, result_library_branch_name)

# Part 3 - Query 1 Creator: Ivan
def part3_query1():
    query_conn = sqlite3.connect('LMS_2.db')
    query_runner = query_conn.cursor()

    try:
        # Check if the 'Late' column exists
        query_runner.execute("PRAGMA table_info(BOOK_LOANS);")
        columns = [column[1] for column in query_runner.fetchall()]
        if 'Late' not in columns:
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

        # Retrieve all records
        query_runner.execute("SELECT * FROM BOOK_LOANS;")
        records = query_runner.fetchall()

        result_book_id = ''
        result_branch_id = ''
        result_card_no = ''
        result_date_out = ''
        result_due_date = ''
        result_returned_date = ''
        result_late = ''

        for record in records:
            result_book_id += str(str(record[0]) + "\n")
            result_branch_id += str(str(record[1]) + "\n")
            result_card_no += str(str(record[2]) + "\n")
            result_date_out += str((record[3]) + "\n")
            result_due_date += str((record[4]) + "\n")
            result_returned_date += str((record[5]) + "\n")
            result_late += str(str(record[6]) + "\n")

        return (result_book_id, result_branch_id, result_card_no, result_date_out, result_due_date, result_returned_date, result_late)
	
    finally:
        query_conn.close() 

# Part 3 - Query 2 Creator: Ivan
def part3_query2():
	query_conn = sqlite3.connect('LMS_2.db')
	query_runner = query_conn.cursor()

	try:
		query_runner.execute("PRAGMA table_info(LIBRARY_BRANCH);")
		columns = [column[1] for column in query_runner.fetchall()]
		if 'LateFee' not in columns:
			query_runner.execute("ALTER TABLE LIBRARY_BRANCH ADD COLUMN LateFee FLOAT DEFAULT 0.00;")


		verified = True
		invalid_message = "The following information is missing/invalid: "

		verify_name = lb_branch_name_entry.get()
		if not verify_name:
			verified = False
			invalid_message += "Library Branch Name. "
		verify_latefee = lb_branch_latefee_entry.get()
		if not verify_latefee:
			verified = False
			invalid_message += "Library Branch Late Fee. "

		query_runner.execute("""
							UPDATE LIBRARY_BRANCH
							SET LateFee = (:latefee)
    						WHERE Branch_Name = (:name);
					   		""", 
								{
									'latefee': float(lb_branch_latefee_entry.get()),
									'name': lb_branch_name_entry.get()
								}
							)
		
		query_conn.commit()
		
		query_runner.execute("SELECT * FROM LIBRARY_BRANCH;")
		records = query_runner.fetchall()

		result_branch_id = ''
		result_branch_name = ''
		result_branch_address = ''
		result_latefee = ''

		for record in records:
			result_branch_id += str(str(record[0]) + "\n")
			result_branch_name += str(record[1] + "\n")
			result_branch_address += str(record[2] + "\n")
			result_latefee += "${:.2f}".format(record[3]) + "\n"

		# Clear the entries
		lb_branch_name_entry.delete(0, END)
		lb_branch_latefee_entry.delete(0, END)

		return (result_branch_id, result_branch_name, result_branch_address, result_latefee)
	
	finally:
		query_conn.close()

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
				THEN '$' || ROUND(CAST((JULIANDAY(BL.Returned_date) - JULIANDAY(BL.Due_Date)) AS INTEGER) * LB.LateFee, 2)
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
				# Format Late Fee Balance to display two decimals if it's not '0'
				if col_index == 9 and value != 0:
					value = "${:.2f}".format(float(value.replace('$', '')))
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
# ==============================TESTING REQUIREMENTS FUNCTIONS ================================= 
# Requirement 1 - Check out a Book
# Creator: Trung Nguyen & Chime Nguyen
def requirement1(query_runner, query_conn):
	# # Clear the old results from the frame 
	for widget in results_frame.grid_slaves():
		widget.grid_forget() # Removes all widgets from the grid from the last query

	# Get input values
	card_no = bl_card_no_entry.get()
	branch_id_or_name = bc_branch_id_entry.get()
	book_id_or_name = b_book_id_entry.get()

	# book_id_to_use = 0
	# branch_id_to_use = 0

	# branch_id = 0
	# book_id = 0
	
	# # Check if the values are valid
	# if ((not card_no) or (not branch_id_or_name) or (not book_id_or_name)):
	# 	return ("Please fill in all fields.", 0, 0)
	

	# # Branch ID Check
	# # Check if branch_id_or_name is a number or a string
	# try:
	# 	# If it's an int, it is a branch id
	# 	branch_id = int(branch_id_or_name)
	# 	is_branch_id = True
	# 	print ("Branch ID")
	# except ValueError:
	# 	# If it's not an int, assume it's a branch name
	# 	branch_id = str(branch_id_or_name)
	# 	is_branch_id = False
	# 	print ("Branch Name")
	
	# print (type(branch_id))


	# # Determine if book_id is ID or Title
	# try:
	# 	# try to convert book_id to an integer
	# 	book_id = int(book_id_or_name)
	# 	is_book_id = True
	# 	print ("Book ID")
	# except ValueError:
	# 	# if it fails, assume it's a string for the title
	# 	book_id = str(book_id_or_name)
	# 	is_book_id = False
	# 	print ("Book Title")

	# print ("Tested for book and branch names.")
	
	# print (type(book_id))

	# # Book 
	# if is_book_id:
	# 	print ("In is_book_id")

	# 	# If it's an ID, Check if the book exists in BOOK_COPIES
	# 	query_runner.execute("SELECT * FROM BOOK_COPIES WHERE Book_Id = ? AND No_Of_Copies > 0", (book_id,))
	# 	available_book = query_runner.fetchone()

	# 	print ("Passed is_book_id execute")
		
	# 	# If the book is not found or available, exit the function
	# 	if not available_book:
	# 		print ("Book not found/available.")
	# 		return ("Book not found/available.", 0, 0)
		
	# 	# Otherwise, the book was found
	# 	print ("Book is found")
	# 	book_id_to_use = book_id
	# else:
	# 	print ("In is_not_book_id")
	# 	# If it's a title, get its ID
	# 	query_runner.execute("SELECT Book_Id FROM BOOK WHERE Title = ?", (book_id_or_name,))
	# 	result = query_runner.fetchone()

	# 	print ("Passed is_not_book_id execute")

	# 	# If the book id was not found based on the title, exit the function
	# 	if result is None:
	# 		print ("Book not found")
	# 		return ("Book not found.", 0, 0)
		
	# 	print ("Book is found")
	# 	book_id_to_use = result[0]

	# 	# Check availability of the book in BOOK_COPIES
	# 	query_runner.execute("SELECT * FROM BOOK_COPIES WHERE Book_Id = ? AND No_Of_Copies > 0", (book_id_to_use,))
	# 	available_book = query_runner.fetchone()[0]

	# 	# If the book is not found or available, exit the function
	# 	if not available_book:
	# 		return ("Book not found/available.", 0, 0)

	
	# # This part checks the branch id or branch name
	# if is_branch_id:
	# 	# if it's a branch id, check if it is a valid branch id

	# 	print (type(branch_id))
	# 	print (type(book_id))
	# 	test = query_runner.execute("SELECT Branch_Name FROM LIBRARY_BRANCH WHERE Branch_Id = (:branchID)",
	# 				{
	# 					'branchID': branch_id
	# 				})
		
	# 	result = test.fetchone()[0]

	# 	if result == None:
	# 		# Otherwise, branch is not available, exit the function
	# 		return ("Branch not available 2", 0, 0)
		
	# 	# Use this branch id for query
	# 	branch_id_to_use = branch_id

	# else:
	# 	# if it's a branch name, check if the branch name has an ID
	# 	print (type(branch_id))
	# 	print (type(book_id))
	# 	test = query_runner.execute("SELECT Branch_Id FROM LIBRARY_BRANCH WHERE Branch_Name = (:branchName)",
	# 						  {
	# 							  'branchName': branch_id
	# 						  })
	# 	result = test.fetchone()[0]

	# 	if result == None:
	# 		# If branch is not available, exit the function
	# 		return ("Branch not found.", 0, 0)

	# 	# Use the result in the first column that contains the branch id
	# 	branch_id_to_use = result

	# # Check if the person has already checked out this book and has not returned it

	# # Create the trigger if it does not exists and have it run after insert
	# # https://www.sqlitetutorial.net/sqlite-trigger/
	# query_runner.execute("""
	# CREATE TRIGGER IF NOT EXISTS reduce_book_copy_on_branch
	# AFTER INSERT ON BOOK_LOANS
	# BEGIN
	# 	UPDATE BOOK_COPIES
	# 	SET No_Of_Copies = No_Of_Copies - 1
	# 	WHERE Branch_Id = NEW.Branch_Id
	# 	AND Book_Id = NEW.Book_Id;
	# END;
	# """)

	# # Commit the trigger into the database	
	# query_conn.commit()

	# # Select the entire table from the BOOK_LOANS table where it matches the exact entry details
	# query_runner.execute("""SELECT * FROM BOOK_LOANS WHERE Book_Id = (:bookID)
	# 				AND Branch_Id = (:branchID) AND Card_No = (:cardNO)""",
	# 				{
	# 					'bookID': book_id,
	# 					'branchID': branch_id,
	# 					'cardNO': card_no 
	# 				})
	
	# # Store the results from the command above into a variable
	# already_loaned = query_runner.fetchall()


	# # In the case that the book was checked out before by the person, check if they have a loan
	# if already_loaned != None:
	# 	# DEBUG: Print the results of the table
	# 	print(already_loaned)
	# 	# Parse the data in each possible row
	# 	for loan in already_loaned:
	# 		loan_returned_date = str(loan[5])
	# 		if loan_returned_date == 'NULL':
	# 			# The book is currently being checked out by the person
	# 			return ("The Borrower Already Has A Loan For This Specific Book In This Branch", 0, 0)
	
	# # Do the checkout now that you have book id and branch id
	# query_runner.execute("""
	# INSERT INTO BOOK_LOANS(Book_Id, Branch_Id, Card_No, Date_Out, Due_Date, Returned_date)
	# VALUES (?, ?, ?, CURRENT_DATE, DATE(CURRENT_DATE, '+1 month'), 'NULL')
	# """, (book_id_to_use, branch_id_to_use, card_no))

	# # DEBUG: Print message that confirms that the new book loan is added
	# print ("Inserted New Book Loan")
	# # Commit the insertion into the database
	# query_conn.commit()

	# # Drop the trigger here after the trigger is executed
	# query_runner.execute("DROP TRIGGER reduce_book_copy_on_branch")
	
	# # Trigger should run automatically if you did after update trigger
	# print ("Trigger Ran")
	
	# # Perform a select query to show the updated table output of book_copies
	# query_runner.execute("""SELECT * FROM BOOK_COPIES""")
	# print ("Selected everything")

	# # Store the results from the command above into a variable
	# results = query_runner.fetchall()

	# # DEBUG: Print the results from the query above
	# print (results)
	# print ("Printed results")

	# # Create a variable that can store multiple strings for each column
	# result_book_id = ''
	# result_branch_id = ''
	# result_no_of_copies = ''

	# # For each part of the data, store them in their respective column
	# for record in results:
	# 	# Store the 1st part of the data in the book ID results in string representation
	# 	result_book_id += str(str(record[0]) + "\n")
	# 	# Store the 2nd part of the data in the branch ID results in string representation
	# 	result_branch_id += str(str(record[1]) + "\n")
	# 	# Store the 3rd part of the data in the number of copies results in string representation
	# 	result_no_of_copies += str(str(record[2]) + "\n")
		
	# # DEBUG: Print the string arrays
	# print (result_book_id)
	# print ('')
	# print (result_branch_id)
	# print ('')
	# print (result_no_of_copies)
	# print ('')

	if not all([card_no, branch_id_or_name, book_id_or_name]):
		return ("Please fill in all fields", 0, 0, 0)

	# Branch ID check
	try:
		branch_id = int(branch_id_or_name)
		is_branch_id = True
	except ValueError:
		branch_id = str(branch_id_or_name)
		is_branch_id = False

	# Determine if book_id is ID or Title
	try:
		if (book_id_or_name == "1984"):
			is_book_id = False
		else:
			book_id = int(book_id_or_name)
			is_book_id = True
	except ValueError:
		book_id = str(book_id_or_name)
		is_book_id = False
	
	# Check Book availability
	if is_book_id:
		query_runner.execute("SELECT * FROM BOOK_COPIES WHERE Book_id = ? AND No_Of_Copies > 0;", (book_id,))
		available_book = query_runner.fetchone()
		if not available_book:
			return ("Book not found/available", 0, 0, 0)
		book_id_to_use = book_id
	else:
		query_runner.execute("SELECT Book_Id FROM BOOK WHERE Title = ?;", (book_id,))
		result = query_runner.fetchone()
		if result is None:
			return ("Book not found", 0, 0, 0)
		book_id_to_use = result[0]
		query_runner.execute("SELECT * FROM BOOK_COPIES WHERE Book_id = ? AND No_Of_Copies > 0;", (book_id_to_use,))
		available_book = query_runner.fetchone()
		if not available_book:
			return ("Book not found/available", 0, 0, 0)

	# Check Branch availability
	if is_branch_id:
		query_runner.execute("SELECT Branch_Name FROM LIBRARY_BRANCH WHERE Branch_Id = ?;", (branch_id,))
		result = query_runner.fetchone()
		if result is None:
			return ("Branch not found", 0, 0, 0)
		branch_id_to_use = branch_id
	else:
		query_runner.execute("SELECT Branch_Id FROM LIBRARY_BRANCH WHERE Branch_Name = ?;", (branch_id,))
		result = query_runner.fetchone()
		if result is None:
			return ("Branch not found", 0, 0, 0)
		branch_id_to_use = result[0]

	# Check if book is available at this branch
	query_runner.execute("""
						SELECT * FROM BOOK_COPIES WHERE Book_Id = ?
						AND Branch_Id = ?
						AND No_Of_Copies > 0;
						""", (book_id_to_use, branch_id_to_use))
	available_at_branch = query_runner.fetchone()
	if not available_at_branch:
		# Clear previous results
		for widget in results_frame.grid_slaves():
			widget.grid_forget() # Removes all widgets from the grid from the last query
		# Display error message
		error_label = Label(results_frame, text="Book Not Available At This Branch")
		error_label.grid(row=RESULTS_ROW, column=0, columnspan=3)
		return ("Book Not Available At This Branch", 0, 0, 0)


	# Check if the person has already checked out this book and has not returned it
	query_runner.execute("""
						SELECT * FROM BOOK_LOANS WHERE Book_Id = ?
						AND Branch_Id = ?
						AND Card_No = ?
						AND Returned_date IS 'NULL';
						""", (book_id_to_use, branch_id_to_use, card_no))
	already_loaned = query_runner.fetchall()
	if already_loaned:
		# Clear previous results
		for widget in results_frame.grid_slaves():
			widget.grid_forget() # Removes all widgets from the grid from the last query
		# Display error message
		error_label = Label(results_frame, text="The Borrower Already Has A Loan For This Specific Book In This Branch")
		error_label.grid(row=RESULTS_ROW, column=0, columnspan=3)
		return ("The Borrower Already Has A Loan For This Specific Book In This Branch", 0, 0, 0)

	# Make the Trigger if it doesn't exist 
	query_runner.execute("""
						CREATE TRIGGER IF NOT EXISTS reduce_book_copy_on_branch
						AFTER INSERT ON BOOK_LOANS
						BEGIN
							UPDATE BOOK_COPIES
							SET No_Of_Copies = No_Of_Copies - 1
							WHERE Branch_Id = NEW.Branch_Id
							AND Book_Id = NEW.Book_Id;
						END;
						""")
	query_conn.commit() # Commit the trigger into the database

	try:
		# Insert the new book loan
		query_runner.execute("""
							INSERT INTO BOOK_LOANS (Book_Id, Branch_Id, Card_No, Date_Out, Due_Date, Returned_date)
							VALUES (?, ?, ?, CURRENT_DATE, DATE(CURRENT_DATE, '+1 month'), 'NULL');
							""", (book_id_to_use, branch_id_to_use, card_no))
		query_conn.commit() # Commit the insertion into the database
	except sqlite3.IntegrityError as e:
		if str(e).startswith('UNIQUE constraint failed'):
			# Clear previous results
			for widget in results_frame.grid_slaves():
				widget.grid_forget() # Removes all widgets from the grid from the last query
			# Display error message
			error_label = Label(results_frame, text="The Borrower Already Has A Loan For This Specific Book In This Branch")
			error_label.grid(row=RESULTS_ROW, column=0, columnspan=3)
			return ("The Borrower Already Has A Loan For This Specific Book In This Branch", 0, 0, 0)
		else:
			raise

	# Display success message
	success_message = f"Success: Book has been checked out by CardNo({card_no}).\n"
	success_label = Label(results_frame, text=success_message)
	success_label.grid(row=RESULTS_ROW-2, column=0, columnspan=3)
		
	# Display the updated table output of book_copies
	query_runner.execute("SELECT * FROM BOOK_COPIES;")
	results = query_runner.fetchall()

	# Store the results into string arrays
	result_book_id = ''
	result_branch_id = ''
	result_no_of_copies = ''

	for record in results:
		result_book_id += str(str(record[0]) + "\n")
		result_branch_id += str(str(record[1]) + "\n")
		result_no_of_copies += str(str(record[2]) + "\n")


	# Clear the entries
	bl_card_no_entry.delete(0, END)
	b_book_id_entry.delete(0, END)
	bc_branch_id_entry.delete(0, END)
	


	# Return the string arrays into the do_query function
	return (result_book_id, result_branch_id, result_no_of_copies)

# Requirement 2 - Sign up a new Borrower
# Creator: Ivan Ko
def requirement2(query_runner, query_conn):
	name = bo_name_entry.get()
	address = bo_address_entry.get()
	phone = bo_phone_entry.get()

	if (not name) or (not address) or (not phone):
		results_label.config(text = "Please fill in all fields")
		results_label.grid(row = 100, column = 0, columnspan = 2)
		return ("Please fill in all fields", 0, 0, 0)
	
	query_runner.execute("SELECT Card_No FROM BORROWER;")
	Result_Card_No = query_runner.fetchall()
	Existing_Card_No = ''

	Existing_Card_No = []
	for number in Result_Card_No:
		Existing_Card_No.append(number[0])
		

	query_runner.execute("SELECT Phone FROM BORROWER;")
	Existing_Phones = query_runner.fetchall()

	
	for exist_phone in Existing_Phones:
		if exist_phone[0] == phone:
			results_label.config(text = "Borrower already added based upon existing phone numbers")
			results_label.grid(row = 100, column = 0, columnspan = 2)
			return ("Borrower already added based upon existing phone numbers", 0, 0, 0)

	while(True):
		generated_card_no = random.randint(100000, 999999)
		if generated_card_no not in Existing_Card_No:
			Card_Number = generated_card_no
			break

	try:
		query_runner.execute("""
					  		INSERT INTO BORROWER (Card_No, Name, Address, Phone) 
					  		VALUES (?, ?, ?, ?);
						""", (Card_Number, name, address, phone))
	
		query_conn.commit()
	except:
		return ("The Borrower Already Added", 0, 0, 0)

	query_runner.execute("SELECT * FROM BORROWER;")
	results = query_runner.fetchall()
	print(results)

	result_card = ''
	result_name = ''
	result_address = ''
	result_phone = ''

	for result in results:
		result_card += str(str(result[0]) + "\n")
		result_name += str(result[1] + "\n")
		result_address += str(result[2] + "\n")
		result_phone += str(result[3] + "\n")

	bo_name_entry.delete(0, END)
	bo_address_entry.delete(0, END)
	bo_phone_entry.delete(0, END)
	return (result_card, result_name, result_address, result_phone)

# Requirement 3 - Add new Book to All Branches
# Creator: Trung Nguyen
def requirement3(query_runner):
	# Clear the old results from the frame
	for widget in results_frame.grid_slaves():
		widget.grid_forget() # Removes all widgets from the grid from the last query

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

	# Get all branch ids
	query_runner.execute("SELECT Branch_Id FROM LIBRARY_BRANCH;")
	branch_ids = query_runner.fetchall()

	# Insert the book into all branches
	for branch_id in branch_ids:
		query_runner.execute("INSERT INTO BOOK_COPIES (Book_Id, Branch_Id, No_Of_Copies) VALUES (?, ?, ?);", (book_id, branch_id[0], 5))
	
	# Clear the entries
	b_title_entry.delete(0, END)
	b_publisher_name_entry.delete(0, END)
	ba_author_name_entry.delete(0, END)

	# Get the results
	query_runner.execute("""
					   	SELECT B.Title AS Book_Title, 
					   		LB.Branch_Name AS Branch_Name,
							BC.No_Of_Copies AS Number_Of_Copies
					   	FROM BOOK B 
							JOIN BOOK_COPIES BC ON B.Book_Id = BC.Book_Id
					   		JOIN LIBRARY_BRANCH LB ON BC.Branch_Id = LB.Branch_Id;
					   """)
	results = query_runner.fetchall()
	
	# Clear the old results from the frame
	for widget in results_frame.grid_slaves():
		widget.grid_forget() # Removes all widgets from the grid from the last query

	results_label.config(text = "Successfully added new book to all branches.")
	results_label.grid(row = 98, column = 0, columnspan = 2)

	book_title_label = Label(results_frame, text = "Book Title\n______________________")
	book_title_label.grid(row = 99, column = 0)
	branch_name_label = Label(results_frame, text = "Branch Name\n______________________")	
	branch_name_label.grid(row = 99, column = 1)
	no_of_copies_label = Label(results_frame, text = "No of Copies\n______________________")
	no_of_copies_label.grid(row = 99, column = 2)

	book_titles= ''
	branch_names = ''
	no_of_copies = ''

	for row in results:
		book_titles += str(row[0] + "\n")
		branch_names += str(row[1] + "\n")
		no_of_copies += str(row[2])+ "\n"

	result_label1 = Label(results_frame, text = book_titles)
	result_label1.grid(row = 100, column = 0)
	result_label2 = Label(results_frame, text = branch_names)
	result_label2.grid(row = 100, column = 1)
	result_label3 = Label(results_frame, text = no_of_copies)
	result_label3.grid(row = 100, column = 2)


	return

# Requirement 4 - Check copies Loaned
# Creator: Trung Nguyen
def requirement4(query_runner):
	
	# Get input values
	book_title = b_title_entry.get()

	# Check if the value are valid
	if not book_title:
		results_label.config(text = "Please fill in all fields.")
		results_label.grid(row = 100, column = 0, columnspan = 2)
		return
	
	# clear previous results
	for widget in results_frame.grid_slaves():
		widget.grid_forget() # Removes all widgets from the grid from the last query

	# Check if book_title is ID or title
	try:
		# try to convert book_id to an integer unless it's 1984
		if (book_title == "1984"):
			is_book_id = False
		else:
			book_id = int(book_title)
			is_book_id = True
	except ValueError:
		# if it fails, assume it's a title
		is_book_id = False

	if is_book_id:
		# If it's an ID, use it directly in query
		query_runner.execute("""
					   SELECT LB.Branch_Name, COUNT(BL.Book_Id) AS Copies_Loaned
					   FROM BOOK_LOANS BL JOIN LIBRARY_BRANCH LB ON BL.Branch_Id = LB.Branch_Id
					   WHERE BL.Book_Id = ? AND BL.Date_Out IS NOT 'NULL'
					   GROUP BY LB.Branch_Name;
					   """, (book_id,))
	else:
		# If it's a title, get its ID
		query_runner.execute("SELECT Book_Id FROM BOOK WHERE Title = ?;", (book_title,))
		book_id = query_runner.fetchone()

		if book_id is None:
			results_label.config(text = "Book not found.")
			results_label.grid(row = 100, column = 0, columnspan = 2)
			return
		
		book_id = book_id[0]

		# Execute query to get the number of copies loaned per branch
		query_runner.execute("""
			SELECT LB.Branch_Name, COUNT(BL.Book_Id) AS Copies_Loaned
			FROM BOOK_LOANS BL JOIN LIBRARY_BRANCH LB ON BL.Branch_Id = LB.Branch_Id
			WHERE BL.Book_Id = ? AND BL.Date_Out IS NOT 'NULL'
			GROUP BY LB.Branch_Name;
			""", (book_id,))

	# Get the results
	results = query_runner.fetchall()

	# Clear old results
	for widget in results_frame.grid_slaves():
		widget.grid_forget() # Removes all widgets from the grid from the last query


	# Display the results
	branch_name = ''
	copies_loaned = ''
	result_branch_name = Label(results_frame, text = "Branch Name\n______________________")
	result_copies_loaned = Label(results_frame, text = "Copies Loaned\n______________________")

	for row in results:
		branch_name += str(row[0] + "\n")
		copies_loaned += str(row[1]) + "\n"

	# Create labels for each array of
	result_label1 = Label(results_frame, text = branch_name)
	result_label2 = Label(results_frame, text = copies_loaned)

	# Display the results using the grid and differing columns
	result_branch_name.grid(row = 99, column = 0)
	result_copies_loaned.grid(row = 99, column = 1)
	result_label1.grid(row = 100, column = 0)
	result_label2.grid(row = 100, column = 1)

	# Clear the entries
	b_title_entry.delete(0, END)
	

	return

# Requirement 5 - Check for Late Returns
# Creator: Trung Nguyen
def requirement5(query_runner):
	start_due_date = bl_date_out_start_entry.get()
	end_due_date = bl_date_out_end_entry.get()

	if not start_due_date or not end_due_date:
		results_label.config(text = "Please fill in all fields.")
		results_label.grid(row = 100, column = 0, columnspan = 2)
		return
	
	# Clear previous results
	for widget in results_frame.grid_slaves():
		widget.grid_forget() # Removes all widgets from the grid from the last query

	# Execute the query
	query_runner.execute("""
					  SELECT B.Title, LB.Branch_Name, BL.Card_no,
					  	CASE WHEN BL.Returned_date IS NOT 'NULL' or NULL THEN
					  		CASE WHEN JULIANDAY(BL.Returned_date) - JULIANDAY(BL.Due_Date) > 0 THEN
					  			CAST(JULIANDAY(BL.Returned_date) - JULIANDAY(BL.Due_Date) AS INTEGER)
					  			ELSE 'Not Late'
							END
					  		WHEN JULIANDAY(CURRENT_DATE) > JULIANDAY(BL.Due_Date) THEN
					  			CAST(JULIANDAY(CURRENT_DATE) - JULIANDAY(BL.Due_Date) AS INTEGER)
					  			ELSE 'Not Late'
					  	END AS Days_Late
					  FROM BOOK_LOANS BL JOIN BOOK B ON BL.Book_Id = B.Book_Id
					  	JOIN LIBRARY_BRANCH LB ON BL.Branch_Id = LB.Branch_Id
					  WHERE BL.Due_Date BETWEEN ? AND ?
						AND (BL.Returned_date IS 'NULL' OR CAST(JULIANDAY(BL.Returned_date) > JULIANDAY(BL.Due_Date) AS INTEGER) > 0)
					  	AND (Days_Late != 'Not Late')
					  ORDER BY B.Title, LB.Branch_Name;
					  """, (start_due_date, end_due_date))
	
	# Get the results
	result = query_runner.fetchall()

	# Display the results
	title = ''
	branch_name = ''
	card_no = ''
	days_late = ''
	result_title = Label(results_frame, text = "Title\n______________________")
	result_branch_name = Label(results_frame, text = "Branch Name\n______________________")
	result_card_no = Label(results_frame, text = "Card No\n______________________")
	result_days_late = Label(results_frame, text = "Days Late\n______________________")
	for row in result:
		title += str(row[0] + "\n")
		branch_name += str(row[1] + "\n")
		card_no += str(row[2]) + "\n"
		days_late += str(row[3]) + "\n"

	# Create labels for each array of
	result_label1 = Label(results_frame, text = title)
	result_label2 = Label(results_frame, text = branch_name)
	result_label3 = Label(results_frame, text = card_no)
	result_label4 = Label(results_frame, text = days_late)
	
	# Display the results using the grid and differing columns
	result_title.grid(row = 99, column = 0)
	result_branch_name.grid(row = 99, column = 1)
	result_card_no.grid(row = 99, column = 2)
	result_days_late.grid(row = 99, column = 3)
	result_label1.grid(row = 100, column = 0)
	result_label2.grid(row = 100, column = 1)
	result_label3.grid(row = 100, column = 2)
	result_label4.grid(row = 100, column = 3)

	# Clear the entries
	bl_date_out_start_entry.delete(0, END)
	bl_date_out_end_entry.delete(0, END)
	


	return

# Requirement 6 - View Info on a Book Loan
# Creator: Trung Nguyen
def requirement6(query_runner):
	# Get input values
	card_no = bl_card_no_entry.get()
	borrower_name = bo_name_entry.get()
	book_id = b_book_id_entry.get()
	book_title = b_title_entry.get()

	# Clear previous results
	for widget in results_frame.grid_slaves():
		widget.grid_forget() # Removes all widgets from the grid from the last query

	# Query based on input criteria
	query = """
		SELECT BOR.Card_No AS Borrower_ID,
			BOR.Name as Borrower_Name,
			B.Title as Book_Title,
			BL.Book_Id as Book_ID,
			CASE
				WHEN BL.Returned_Date IS NOT 'NULL' OR NULL THEN
					CASE
						WHEN JULIANDAY(BL.Returned_Date) - JULIANDAY(BL.Due_Date) > 0 THEN
							'$' || ROUND((JULIANDAY(BL.Returned_Date) - JULIANDAY(BL.Due_Date)) * LB.LateFee, 2)
						ELSE 'Non-Applicable'
					END
				WHEN JULIANDAY(CURRENT_DATE) > JULIANDAY(BL.Due_Date) THEN
					'$' || ROUND((JULIANDAY(CURRENT_DATE) - JULIANDAY(BL.Due_Date)) * LB.LateFee, 2)
				ELSE 'Non-Applicable'
			END AS Late_Fee_Ammount
		FROM BORROWER BOR
			JOIN BOOK_LOANS BL ON BOR.Card_No = BL.Card_No
			JOIN BOOK B ON BL.Book_Id = B.Book_Id
			JOIN LIBRARY_BRANCH LB ON BL.Branch_Id = LB.Branch_Id
	"""
	conditions = []
	params = []

	if card_no:
		conditions.append("BOR.Card_No = ?")
		params.append(card_no)
	
	if book_id:
		try:
			book_id = int(book_id)
			conditions.append("BL.Book_Id = ?")
			params.append(book_id)
		except ValueError:
			results_label.config(text = "Invalid Book ID.")
			results_label.grid(row = 100, column = 0, columnspan = 2)
			return
	
	if book_title:
		conditions.append("B.Title LIKE ?")
		params.append(f"%{book_title}%")

	if borrower_name: 
		conditions.append("BOR.Name LIKE ?")
		params.append(f"%{borrower_name}%")

	# Add the conditions to the query
	if conditions:
		query += " WHERE " + " AND ".join(conditions)

	# Order by late fee amount
	query += """ 
		ORDER BY 
			CASE 
				WHEN Late_Fee_Ammount = 'Non-Applicable' THEN 0
			END,
			CAST(SUBSTR(Late_Fee_Ammount, 2) AS FLOAT) DESC; -- gets the substring strarting from index 2 then orders it
	"""
	 
	# Execute the query
	query_runner.execute(query, params)

	# Get the results
	results = query_runner.fetchall()

	# Display the results
	borrower_id = ''
	borrower_name = ''
	book_title = ''
	book_id = ''
	late_fee_amount = ''
	result_borrower_id = Label(results_frame, text = "Borrower ID\n______________________")
	result_borrower_name = Label(results_frame, text = "Borrower Name\n______________________")
	result_book_title = Label(results_frame, text = "Book Title\n______________________")
	result_book_id = Label(results_frame, text = "Book ID\n______________________")
	result_late_fee_amount = Label(results_frame, text = "Late Fee Amount\n______________________")

	for row in results:
		borrower_id += str(row[0]) + "\n"
		borrower_name += str(row[1] + "\n")
		book_title += str(row[2] + "\n")
		book_id += str(row[3]) + "\n"
		late_fee_amount += str(row[4]) + "\n"
		
	# Create labels for each array of
	result_label1 = Label(results_frame, text = borrower_id)
	result_label2 = Label(results_frame, text = borrower_name)
	result_label3 = Label(results_frame, text = book_title)
	result_label4 = Label(results_frame, text = book_id)
	result_label5 = Label(results_frame, text = late_fee_amount)

	# Display the results using the grid and differing columns
	result_borrower_id.grid(row = 99, column = 0)
	result_borrower_name.grid(row = 99, column = 1)
	result_book_title.grid(row = 99, column = 2)
	result_book_id.grid(row = 99, column = 3)
	result_late_fee_amount.grid(row = 99, column = 4)
	result_label1.grid(row = 100, column = 0)
	result_label2.grid(row = 100, column = 1)
	result_label3.grid(row = 100, column = 2)
	result_label4.grid(row = 100, column = 3)
	result_label5.grid(row = 100, column = 4)

	# Clear the entries
	bl_card_no_entry.delete(0, END)
	b_book_id_entry.delete(0, END)
	b_title_entry.delete(0, END)
	bo_name_entry.delete(0, END)


	return

def requirement6a(query_runner):
	# Get input values
	card_no = bl_card_no_entry.get()
	borrower_name = bo_name_entry.get()

	# Clear previous results
	for widget in results_frame.grid_slaves():
		widget.grid_forget() # Removes all widgets from the grid from the last query

	# Query to retrieve borrowers and late fees
	query = """
		SELECT BOR.Card_No AS Borrower_ID,
			BOR.Name AS Borrower_Name,
			CASE
            WHEN BL.Returned_Date IS NOT NULL THEN
                CASE
                    WHEN JULIANDAY(BL.Returned_Date) - JULIANDAY(BL.Due_Date) > 0 THEN
                        CAST(JULIANDAY(BL.Returned_Date) - JULIANDAY(BL.Due_Date) AS INTEGER)
                    ELSE 0
                END
            WHEN BL.Returned_Date IS NULL AND JULIANDAY(CURRENT_DATE) > JULIANDAY(BL.Due_Date) THEN
                CAST(JULIANDAY(CURRENT_DATE) - JULIANDAY(BL.Due_Date) AS INTEGER)
            ELSE 0
        END AS Days_Late,
        ROUND(SUM(CASE
                    WHEN BL.Returned_Date IS NOT NULL AND JULIANDAY(BL.Returned_Date) - JULIANDAY(BL.Due_Date) > 0 THEN
                        (JULIANDAY(BL.Returned_Date) - JULIANDAY(BL.Due_Date)) * LB.LateFee
                    WHEN BL.Returned_Date IS NULL AND JULIANDAY(CURRENT_DATE) > JULIANDAY(BL.Due_Date) THEN
                        (JULIANDAY(CURRENT_DATE) - JULIANDAY(BL.Due_Date)) * LB.LateFee
                    ELSE 0
				END), 2) AS Total_Fee_Balance
		FROM BORROWER BOR
			JOIN BOOK_LOANS BL ON BOR.Card_No = BL.Card_No
			JOIN LIBRARY_BRANCH LB ON BL.Branch_Id = LB.Branch_Id
	
		"""
	# Additional conditions and parameters for the query
	conditions = []
	params = []

	# Add conditions based on input values
	if card_no:
		conditions.append("BOR.Card_No = ?")
		params.append(card_no)

	# Borrower names that are LIKE the input value
	if borrower_name:
		conditions.append("BOR.Name LIKE ?")
		params.append(f"%{borrower_name}%")
	
	# Add the conditions to the query
	if conditions:
		query += " WHERE " + " AND ".join(conditions)

	# Group by borrower and order by total fee balance
	query += " GROUP BY BOR.Card_No, BOR.Name ORDER BY Total_Fee_Balance DESC;"

	# Execute the query
	query_runner.execute(query, params)

	# Get the results
	results = query_runner.fetchall()

	# Display the results
	borrower_id = ''
	borrower_name_displayed = ''
	days_late_displayed = ''
	total_fee_balance = ''

	result_borrower_id = Label(results_frame, text = "Borrower ID\n______________________")
	result_borrower_name = Label(results_frame, text = "Borrower Name\n______________________")
	result_days_late = Label(results_frame, text = "Days Late\n______________________")
	result_total_fee_balance = Label(results_frame, text = "Total Fee Balance\n______________________")

	for row in results:
		borrower_id += str(row[0]) + "\n"
		borrower_name_displayed += str(row[1]) + "\n"
		days_late_displayed += str(row[2]) + "\n"
		total_fee_balance += f"${row[3]:.2f}\n" if row[3] > 0 else "$0.00\n"

	# Create labels for each array of results
	result_label1 = Label(results_frame, text = borrower_id)
	result_label2 = Label(results_frame, text = borrower_name_displayed)
	result_label3 = Label(results_frame, text = days_late_displayed)
	result_label4 = Label(results_frame, text = total_fee_balance)

	# Display the results using the grid and differing columns
	result_borrower_id.grid(row = 99, column = 0)
	result_borrower_name.grid(row = 99, column = 1)
	result_days_late.grid(row = 99, column = 2)
	result_total_fee_balance.grid(row = 99, column = 3)
	result_label1.grid(row = 100, column = 0)
	result_label2.grid(row = 100, column = 1)
	result_label3.grid(row = 100, column = 2)
	result_label4.grid(row = 100, column = 3)
	
	# Clear the entries
	bl_card_no_entry.delete(0, END)
	bo_name_entry.delete(0, END)

	return

def requirement6b(query_runner):
	# Get input values
	card_no = bl_card_no_entry.get()
	book_id = b_book_id_entry.get()
	book_title = b_title_entry.get()

	# Clear previous results
	for widget in results_frame.grid_slaves():
		widget.grid_forget() # Removes all widgets from the grid from the last query

	# Query to retrieve books and late fees
	query = """
		SELECT B.Title AS Book_Title,
			BL.Book_Id AS Book_ID,
			CASE
				WHEN BL.Returned_Date IS NOT 'NULL' OR NULL THEN
					CASE
						WHEN JULIANDAY(BL.Returned_Date) - JULIANDAY(BL.Due_Date) > 0 THEN
							'$' || ROUND((JULIANDAY(BL.Returned_Date) - JULIANDAY(BL.Due_Date)) * LB.LateFee, 2)
						ELSE 'Non-Applicable'
					END
				WHEN JULIANDAY(CURRENT_DATE) > JULIANDAY(BL.Due_Date) THEN
					'$' || ROUND((JULIANDAY(CURRENT_DATE) - JULIANDAY(BL.Due_Date)) * LB.LateFee, 2)
				ELSE 'Non-Applicable'
			END AS Late_Fee_Amount
		FROM BOOK B
			JOIN BOOK_LOANS BL ON B.Book_Id = BL.Book_Id
			JOIN LIBRARY_BRANCH LB ON BL.Branch_Id = LB.Branch_Id
		
	"""

	# Additional conditions and parameters for the query
	params = []

	if card_no:
		query += " WHERE BL.Card_No = ?"
		params.append(card_no)

	if book_id:
		try:
			book_id = int(book_id)
			query += " AND BL.Book_Id = ?"
			params.append(book_id)
		except ValueError:
			results_label.config(text = "Invalid Book ID.")
			results_label.grid(row = 100, column = 0, columnspan = 2)
			return
		
	if book_title:
		query += " AND B.Title LIKE ?"
		params.append(f"%{book_title}%")


	# Order by late fee amount
	query += """
		ORDER BY 
			CASE 
				WHEN Late_Fee_Amount = 'Non-Applicable' THEN 0 
			END, 
			CAST(SUBSTR(Late_Fee_Amount, 2) AS FLOAT) DESC; -- Gets the substring starting from index 2 the orders it
	"""

	# Execute the query
	query_runner.execute(query, params)

	# Get the results
	results = query_runner.fetchall()

	# Display the results
	book_title_displayed = ''
	book_id_displayed = ''
	late_fee_amount = ''

	result_book_title = Label(results_frame, text = "Book Title\n______________________")
	result_book_id = Label(results_frame, text = "Book ID\n______________________")
	result_late_fee_amount = Label(results_frame, text = "Late Fee Amount\n______________________")

	for row in results:
		book_title_displayed += str(row[0]) + "\n"
		book_id_displayed += str(row[1]) + "\n"
		late_fee_amount += str(row[2]) + "\n"

	# Create labels for each array of results
	result_label1 = Label(results_frame, text = book_title_displayed)
	result_label2 = Label(results_frame, text = book_id_displayed)
	result_label3 = Label(results_frame, text = late_fee_amount)

	# Display the results using the grid and differing columns
	result_book_title.grid(row = 99, column = 0)
	result_book_id.grid(row = 99, column = 1)
	result_late_fee_amount.grid(row = 99, column = 2)
	result_label1.grid(row = 100, column = 0)
	result_label2.grid(row = 100, column = 1)
	result_label3.grid(row = 100, column = 2)

	# Clear the entries
	b_book_id_entry.delete(0, END)
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
		(result_card, result_name, result_address, result_phone) = part2_query1(query_runner)
		
		if(result_name != 0):
			results0a = Label(results_frame, text = "Card No", justify = "left")
			results0b = Label(results_frame, text = "Borrower Name", justify = "left")
			results0c = Label(results_frame, text = "Borrower Address", justify = "left")
			results0d = Label(results_frame, text = "Borrower Phone", justify = "left")

			results1 = Label(results_frame, text = result_card, justify = "left")
			results2 = Label(results_frame, text = result_name, justify = "left")
			results3 = Label(results_frame, text = result_address, justify = "left")
			results4 = Label(results_frame, text = result_phone, justify = "left")


			results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 22, sticky = "w")
			results0b.grid(row = RESULTS_ROW-1, column = 1, padx = 22, sticky = "w")
			results0c.grid(row = RESULTS_ROW-1, column = 2, padx = 22, sticky = "w")
			results0d.grid(row = RESULTS_ROW-1, column = 3, padx = 22, sticky = "w")

			results1.grid(row = RESULTS_ROW, column = 0, padx = 22, sticky = "w")
			results2.grid(row = RESULTS_ROW, column = 1, padx = 22, sticky = "w")
			results3.grid(row = RESULTS_ROW, column = 2, padx = 22, sticky = "w")
			results4.grid(row = RESULTS_ROW, column = 3, padx = 22, sticky = "w")
		else:
			results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 22, sticky = "w")

	elif clicked.get() == query_options[3]:
		# Do computations for Part 2 - Query 2
		(result_card, result_name, result_address, result_phone) = part2_query2(query_runner)
		
		if(result_name != 0):
			results0a = Label(results_frame, text = "Card No", justify = "left")
			results0b = Label(results_frame, text = "Borrower Name", justify = "left")
			results0c = Label(results_frame, text = "Borrower Address", justify = "left")
			results0d = Label(results_frame, text = "Borrower Phone", justify = "left")

			results1 = Label(results_frame, text = result_card, justify = "left")
			results2 = Label(results_frame, text = result_name, justify = "left")
			results3 = Label(results_frame, text = result_address, justify = "left")
			results4 = Label(results_frame, text = result_phone, justify = "left")


			results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 22, sticky = "w")
			results0b.grid(row = RESULTS_ROW-1, column = 1, padx = 22, sticky = "w")
			results0c.grid(row = RESULTS_ROW-1, column = 2, padx = 22, sticky = "w")
			results0d.grid(row = RESULTS_ROW-1, column = 3, padx = 22, sticky = "w")

			results1.grid(row = RESULTS_ROW, column = 0, padx = 22, sticky = "w")
			results2.grid(row = RESULTS_ROW, column = 1, padx = 22, sticky = "w")
			results3.grid(row = RESULTS_ROW, column = 2, padx = 22, sticky = "w")
			results4.grid(row = RESULTS_ROW, column = 3, padx = 22, sticky = "w")
		else:
			results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 22, sticky = "w")

	elif clicked.get() == query_options[4]:
		# Do computations for Part 2 - Query 3
		(result_bookId, result_branchId, result_copies) = part2_query3(query_runner)
		if(result_branchId != 0):
			results0a = Label(results_frame, text = "Book Id", justify = "left")
			results0b = Label(results_frame, text = "Branch Id", justify = "left")
			results0c = Label(results_frame, text = "No of Copies", justify = "left")

			results1 = Label(results_frame, text = result_bookId, justify = "left")
			results2 = Label(results_frame, text = result_branchId, justify = "left")
			results3 = Label(results_frame, text = result_copies, justify = "left")


			results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 22, sticky = "w")
			results0b.grid(row = RESULTS_ROW-1, column = 1, padx = 22, sticky = "w")
			results0c.grid(row = RESULTS_ROW-1, column = 2, padx = 22, sticky = "w")

			results1.grid(row = RESULTS_ROW, column = 0, padx = 22, sticky = "w")
			results2.grid(row = RESULTS_ROW, column = 1, padx = 22, sticky = "w")
			results3.grid(row = RESULTS_ROW, column = 2, padx = 22, sticky = "w")
		else:
			results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 22, sticky = "w")

	elif clicked.get() == query_options[5]:
		# Do computations for Part 2 - Query 4a
		(result_title, result_Pname, result_Aname) = part2_query4a(query_runner)
		if(result_Pname != 0):
			results0a = Label(results_frame, text = "Title", justify = "left")
			results0b = Label(results_frame, text = "Publisher Name", justify = "left")
			results0c = Label(results_frame, text = "Author Name", justify = "left")

			results1 = Label(results_frame, text = result_title, justify = "left")
			results2 = Label(results_frame, text = result_Pname, justify = "left")
			results3 = Label(results_frame, text = result_Aname, justify = "left")


			results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 22, sticky = "w")
			results0b.grid(row = RESULTS_ROW-1, column = 1, padx = 22, sticky = "w")
			results0c.grid(row = RESULTS_ROW-1, column = 2, padx = 22, sticky = "w")

			results1.grid(row = RESULTS_ROW, column = 0, padx = 22, sticky = "w")
			results2.grid(row = RESULTS_ROW, column = 1, padx = 22, sticky = "w")
			results3.grid(row = RESULTS_ROW, column = 2, padx = 22, sticky = "w")
		else:
			results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 22, sticky = "w")

	elif clicked.get() == query_options[6]:
		# Do computations for Part 2 - Query 4b
		(result_branch_id, result_branch_name, result_branch_address) = part2_query4b(query_runner)
		if(result_branch_name != 0):
			results0a = Label(results_frame, text = "Branch Id", justify = "left")
			results0b = Label(results_frame, text = "Branch Name", justify = "left")
			results0c = Label(results_frame, text = "Branch Address", justify = "left")

			results1 = Label(results_frame, text = result_branch_id, justify = "left")
			results2 = Label(results_frame, text = result_branch_name, justify = "left")
			results3 = Label(results_frame, text = result_branch_address, justify = "left")

			results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 2)
			results0b.grid(row = RESULTS_ROW-1, column = 1, padx = 2)
			results0c.grid(row = RESULTS_ROW-1, column = 2, padx = 2)

			results1.grid(row = RESULTS_ROW, column = 0, padx = 2, sticky = "w")
			results2.grid(row = RESULTS_ROW, column = 1, padx = 2, sticky = "w")
			results3.grid(row = RESULTS_ROW, column = 2, padx = 2, sticky = "w")
		else:
			results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 22, sticky = "w")

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
		(result_borrower_name, result_book_title, result_Author, result_Date_out) = part2_query9(query_runner)

		# Create seperate labels for displaying results separately
		results0a = Label(results_frame, text = "Borrower Name", justify = "left")
		results0b = Label(results_frame, text = "Book Title", justify = "left")
		results0c = Label(results_frame, text = "Author", justify = "left")
		results0d = Label(results_frame, text = "Date Out", justify = "left")

		results1 = Label(results_frame, text = result_borrower_name, justify = "left")
		results2 = Label(results_frame, text = result_book_title, justify = "left")
		results3 = Label(results_frame, text = result_Author, justify = "left")
		results4 = Label(results_frame, text = result_Date_out, justify = "left")

		# Add the results of the query into the grid and display them properly
		results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 2)
		results0b.grid(row = RESULTS_ROW-1, column = 1, padx = 2)
		results0c.grid(row = RESULTS_ROW-1, column = 2, padx = 2)
		results0d.grid(row = RESULTS_ROW-1, column = 3, padx = 2)

		results1.grid(row = RESULTS_ROW, column = 0, padx = 2, sticky = "w")
		results2.grid(row = RESULTS_ROW, column = 1, padx = 2, sticky = "w")
		results3.grid(row = RESULTS_ROW, column = 2, padx = 2, sticky = "w")
		results4.grid(row = RESULTS_ROW, column = 3, padx = 2, sticky = "w")

	elif clicked.get() == query_options[12]:
		# Do computations for Part 2 - Query 10
		(result_borrower_name, result_borrower_address, result_library_branch_name) = part2_query10(query_runner)
		
		results0a = Label(results_frame, text = "Borrower Name", justify = "left")
		results0b = Label(results_frame, text = "Borrower Address", justify = "left")
		results0c = Label(results_frame, text = "Branch Name", justify = "left")

		results1 = Label(results_frame, text = result_borrower_name, justify = "left")
		results2 = Label(results_frame, text = result_borrower_address, justify = "left")
		results3 = Label(results_frame, text = result_library_branch_name, justify = "left")


		results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 2)
		results0b.grid(row = RESULTS_ROW-1, column = 1, padx = 2)
		results0c.grid(row = RESULTS_ROW-1, column = 2, padx = 2)

		results1.grid(row = RESULTS_ROW, column = 0, padx = 2, sticky = "w")
		results2.grid(row = RESULTS_ROW, column = 1, padx = 2, sticky = "w")
		results3.grid(row = RESULTS_ROW, column = 2, padx = 2, sticky = "w")

	elif clicked.get() == query_options[15]:
		# Do computations for Part 3 - Query 1
		(result_book_id, result_branch_id, result_card_no, result_date_out, result_due_date, result_returned_date, result_late) = part3_query1()
		
		results0a = Label(results_frame, text = "Book Id", justify = "left")
		results0b = Label(results_frame, text = "Branch Id", justify = "left")
		results0c = Label(results_frame, text = "Card Number", justify = "left")
		results0d = Label(results_frame, text = "Date Out", justify = "left")
		results0e = Label(results_frame, text = "Due Date", justify = "left")
		results0f = Label(results_frame, text = "Returned Date", justify = "left")
		results0g = Label(results_frame, text = "Late", justify = "left")

		results1 = Label(results_frame, text = result_book_id, justify = "left")
		results2 = Label(results_frame, text = result_branch_id, justify = "left")
		results3 = Label(results_frame, text = result_card_no, justify = "left")
		results4 = Label(results_frame, text = result_date_out, justify = "left")
		results5 = Label(results_frame, text = result_due_date, justify = "left")
		results6 = Label(results_frame, text = result_returned_date, justify = "left")
		results7 = Label(results_frame, text = result_late, justify = "left")
		

		results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 2)
		results0b.grid(row = RESULTS_ROW-1, column = 1, padx = 2)
		results0c.grid(row = RESULTS_ROW-1, column = 2, padx = 2)
		results0d.grid(row = RESULTS_ROW-1, column = 3, padx = 2)
		results0e.grid(row = RESULTS_ROW-1, column = 4, padx = 2)
		results0f.grid(row = RESULTS_ROW-1, column = 5, padx = 2)
		results0g.grid(row = RESULTS_ROW-1, column = 6, padx = 2)

		results1.grid(row = RESULTS_ROW, column = 0, padx = 2, sticky = "w")
		results2.grid(row = RESULTS_ROW, column = 1, padx = 2, sticky = "w")
		results3.grid(row = RESULTS_ROW, column = 2, padx = 2, sticky = "w")
		results4.grid(row = RESULTS_ROW, column = 3, padx = 2, sticky = "w")
		results5.grid(row = RESULTS_ROW, column = 4, padx = 2, sticky = "w")
		results6.grid(row = RESULTS_ROW, column = 5, padx = 2, sticky = "w")
		results7.grid(row = RESULTS_ROW, column = 6, padx = 2, sticky = "w")
		
	

	elif clicked.get() == query_options[16]:
		# Do computations for Part 3 - Query 2
		(result_branch_id, result_branch_name, result_branch_address, result_latefee) = part3_query2()

		results0a = Label(results_frame, text = "Branch Id", justify = "left")
		results0b = Label(results_frame, text = "Branch Name", justify = "left")
		results0c = Label(results_frame, text = "Branch Address", justify = "left")
		results0d = Label(results_frame, text = "Late Fee", justify = "left")

		results1 = Label(results_frame, text = result_branch_id, justify = "left")
		results2 = Label(results_frame, text = result_branch_name, justify = "left")
		results3 = Label(results_frame, text = result_branch_address, justify = "left")
		results4 = Label(results_frame, text = result_latefee, justify = "left")

		results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 2)
		results0b.grid(row = RESULTS_ROW-1, column = 1, padx = 2)
		results0c.grid(row = RESULTS_ROW-1, column = 2, padx = 2)
		results0d.grid(row = RESULTS_ROW-1, column = 3, padx = 2)

		results1.grid(row = RESULTS_ROW, column = 0, padx = 2, sticky = "w")
		results2.grid(row = RESULTS_ROW, column = 1, padx = 2, sticky = "w")
		results3.grid(row = RESULTS_ROW, column = 2, padx = 2, sticky = "w")
		results4.grid(row = RESULTS_ROW, column = 3, padx = 2, sticky = "w")


	elif clicked.get() == query_options[17]:
		# Do computations for Part 3 - Query 3
		results_text = part3_query3(query_runner)
		results_label.config(text = results_text)

#	==================================== TESTING REQUIREMENTS FUNCTIONS =================================

	elif clicked.get() == query_options[22]:
		# Do computations for Requirement 1
		(result_book_id, result_branch_id, result_no_of_copies) = requirement1(query_runner, query_conn)
		if (result_branch_id == 0) or (result_no_of_copies == 0):
			# Return error message if there was an error
			results_label.config(text = "Error: Book ID not found at Branch.")
		else:
			# Create seperate labels for displaying results separately
			results0a = Label(results_frame, text = "Book ID\n______________________", justify = "center")
			results0b = Label(results_frame, text = "Branch ID\n______________________", justify = "center")
			results0c = Label(results_frame, text = "Number Of Copies\n______________________", justify = "center")

			results1 = Label(results_frame, text = result_book_id, justify = "center")
			results2 = Label(results_frame, text = result_branch_id, justify = "center")
			results3 = Label(results_frame, text = result_no_of_copies, justify = "center")

			# Add the results of the query into the grid and display them properly
			results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 22, sticky = "nsew")
			results0b.grid(row = RESULTS_ROW-1, column = 1, padx = 22, sticky = "nsew")
			results0c.grid(row = RESULTS_ROW-1, column = 2, padx = 22, sticky = "nsew")

			results1.grid(row = RESULTS_ROW, column = 0, padx = 22, sticky = "nsew")
			results2.grid(row = RESULTS_ROW, column = 1, padx = 22, sticky = "nsew")
			results3.grid(row = RESULTS_ROW, column = 2, padx = 22, sticky = "nsew")

	elif clicked.get() == query_options[23]:
		# Do computations for Requirement 2
		(result_card, result_name, result_address, result_phone) = requirement2(query_runner, query_conn)
		
		if(result_name != 0):
			results0a = Label(results_frame, text = "Card No", justify = "left")
			results0b = Label(results_frame, text = "Borrower Name", justify = "left")
			results0c = Label(results_frame, text = "Borrower Address", justify = "left")
			results0d = Label(results_frame, text = "Borrower Phone", justify = "left")

			results1 = Label(results_frame, text = result_card, justify = "left")
			results2 = Label(results_frame, text = result_name, justify = "left")
			results3 = Label(results_frame, text = result_address, justify = "left")
			results4 = Label(results_frame, text = result_phone, justify = "left")


			results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 22, sticky = "w")
			results0b.grid(row = RESULTS_ROW-1, column = 1, padx = 22, sticky = "w")
			results0c.grid(row = RESULTS_ROW-1, column = 2, padx = 22, sticky = "w")
			results0d.grid(row = RESULTS_ROW-1, column = 3, padx = 22, sticky = "w")

			results1.grid(row = RESULTS_ROW, column = 0, padx = 22, sticky = "w")
			results2.grid(row = RESULTS_ROW, column = 1, padx = 22, sticky = "w")
			results3.grid(row = RESULTS_ROW, column = 2, padx = 22, sticky = "w")
			results4.grid(row = RESULTS_ROW, column = 3, padx = 22, sticky = "w")
		else:
			results0a.grid(row = RESULTS_ROW-1, column = 0, padx = 22, sticky = "w")

	elif clicked.get() == query_options[24]:
		# Do computations for Requirement 3
		results_text = requirement3(query_runner)
		results_label.config(text = results_text)

	elif clicked.get() == query_options[25]:
		# Do computations for Requirement 4
		results_text = requirement4(query_runner)
		results_label.config(text = results_text)

	elif clicked.get() == query_options[26]:
		# Do computations for Requirement 5
		results_text = requirement5(query_runner)
		results_label.config(text = results_text)

	elif clicked.get() == query_options[27]:
		# Do computations for GENERALIZED Requirement 6
		results_text = requirement6(query_runner)
		results_label.config(text = results_text)

	elif clicked.get() == query_options[28]:
		# Do computations for Requirement 6a
		results_text = requirement6a(query_runner)
		results_label.config(text = results_text)
	
	elif clicked.get() == query_options[29]:
		# Do computations for Requirement 6b
		results_text = requirement6b(query_runner)
		results_label.config(text = results_text)

# ==================================== END OF TESTING REQUIREMENTS FUNCTIONS =================================

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
lb_branch_latefee_label = Label(textfield_frame, text = "Library Branch's Late Fee", width = 30)

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
lb_branch_latefee_entry = Entry(textfield_frame, width = 30)

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