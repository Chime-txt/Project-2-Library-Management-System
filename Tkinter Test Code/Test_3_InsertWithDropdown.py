from tkinter import *

# Aliases For Referencing The Entries And Tables
# PUBLISHER p
# LIBRARY_BRANCH lb
# BORROWER bo
# BOOK b
# BOOK_LOANS bl
# BOOK_COPIES bc
# BOOK_AUTHOR ba

# ======================================== Creating Windows ========================================

root = Tk()
root.title('Library Management System')
root.geometry("600x400")
root.minsize(600, 250) # Set the minumum size of window to 600 px (width) by 250 px (height)
root.maxsize(600, 800) # Set the maximum size of window to 600 px (width) by 800 px (height)

# ================================  Frames  ================================

# Create 0th frame for the Title only
title_frame = LabelFrame(root, borderwidth = 0, pady = 5)
title_frame.pack(side = "top", anchor = "center")

# Create 1st frame for the dropdown menu
dropdown_frame = LabelFrame(root, borderwidth = 0, pady = 5)
dropdown_frame.pack()

# Create 2nd frame for each query
frame = Frame(root, borderwidth = 0, padx = 5, pady = 5)
frame.pack(padx = 2)

# ======================================== Dropdown Options ========================================

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


# ======================================== Function Command ========================================

# Command for selected dropdown menu, where event checks for changes in dropdown
def select_from_dropdown(event):
	# myLabel = Label(root).pack()
	for widget in frame.grid_slaves():
		if int(widget.grid_info()["row"]) > 1:
			widget.grid_forget()
	# The Create Database dropdown is not necessary, but an option to recreate the database could be
	# an option if we need to test other stuff with the query.
	if clicked.get() == "Part 2 - Query 1":
		# Query 1 - Add New Borrower
		query1_label = Label(frame, text = "Insert New Borrower Into Database")
		query1_label.grid(row = 3, column = 0, columnspan = 2)

		# Textbox Fields
		bo_name = Entry(frame, width = 30)
		bo_name.grid(row = 4, column = 1)

		bo_address = Entry(frame, width = 30)
		bo_address.grid(row = 5, column = 1)

		bo_phone = Entry(frame, width = 30)
		bo_phone.grid(row = 6, column = 1)

		# Textbox Labels
		bo_name_label = Label(frame, text = "Borrower's Name")
		bo_name_label.grid(row = 4, column = 0, sticky = "w")

		bo_address_label = Label(frame, text = "Borrower's Address")
		bo_address_label.grid(row = 5, column = 0, sticky = "w")

		bo_phone_label = Label(frame, text = "Borrower's Phone")
		bo_phone_label.grid(row = 6, column = 0, sticky = "w")

	elif clicked.get() == "Part 2 - Query 2":
		# Query 2 - Update Phone Number Of Borrower
		query2_label = Label(frame, text = "Update A Borrower's Phone Number")
		query2_label.grid(row = 3, column = 0, columnspan = 2)
	else:
		select_label = Label(frame, text = "Select the query using the dropdown above.")
		select_label.grid(row = 2, column = 0)

# ======================================== Widget & Griding ========================================
# You grid the functionalities inside of the frames (not the root), and then you pack the frames.
# Alternatively, you can grid some functionalities in the frames, pack the frames, and then pack
#	any other functionalities outside of the frames.
# However, if we are not going to use frames, then we can abandon the idea of packing and just
#	use grid as it is easier to work with and the professor used grid for the demonstration GUI.

# Place title of database system at the top using the frame
title = Label(title_frame, text = "Library Management System",
	  background = "blue", foreground = "white",
	  justify = "center", anchor = "center", padx = 224,
	  pady = 5)
title.grid(row = 0, columnspan = 10)

# Dropdown
clicked = StringVar()
clicked.set(query_options[0])

dropdown = OptionMenu(dropdown_frame, clicked, *query_options, command = select_from_dropdown)
dropdown.grid(row = 1)

# ====================================== Commands 3 - Packing ======================================
# This is an example of why functionalities in the root are unable to use grid, but instead uses
#	pack as it will cause an error where Tkinter's geometry manager grid cannot be used due to
#	already having stuff in the root being managed by some pack(s).

# We cannot use grid here since in the root, there were stuff that we already packed
myButton = Button(root, text = "Select From List")
myButton.pack()

footer = Label(root, text = "Created By Group 2 - Chime Nguyen, Ivan Ko, Trung Nguyen",
	  background = "blue", foreground = "white",
	  justify = "center", anchor = "center", padx = 224,
	  pady = 5)
footer.pack(side = "bottom", anchor = "center")

# ============================================== Main ==============================================

select_label = Label(frame, text = "Select the query using the dropdown above.")
select_label.grid(row = 2, column = 0)

root.mainloop()

# ============================================= Credit =============================================

# If we use this feature, we will need to add the following references:
#
# Adding Frames To Your Program - Python Tkinter GUI Tutorial #11
# https://youtu.be/_auZ8TTkojQ
#
# Python | forget_pack() and forget_grid() method in Tkinter by GeeksForGeeks 
# https://www.geeksforgeeks.org/python-forget_pack-and-forget_grid-method-in-tkinter/