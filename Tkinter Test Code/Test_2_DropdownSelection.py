from tkinter import *

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
dropdown_frame.pack(padx = 10)

# Create 2nd frame for each query
frame = Frame(root, borderwidth = 0, padx = 5, pady = 5)
frame.pack(padx = 10)

# ======================================== Dropdown Options ========================================

# Query options for dropdown
query_options = [
	"Create Database",
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
	"Part 3 - Query 1",
	"Part 3 - Query 2",
	"Part 3 - Query 3",
]


# ======================================== Function Command ========================================

# Command for selected dropdown menu
def select_from_dropdown(event):
	# myLabel = Label(root).pack()
	for widget in frame.grid_slaves():
		if int(widget.grid_info()["row"]) > 1:
			widget.grid_forget()
	if clicked.get() == "Create Database":
		# Replace this with a function that will do the rest of the stuff
		b = Button(frame, text="Don't Click On Me")
		b.grid(row = 2, column = 0)
	elif clicked.get() == "Part 2 - Query 1":
		# Replace this with a function that will do the rest of the stuff
		b = Button(frame, text = "Hi Query 1")
		b.grid(row = 2, column = 0)
	else:
		b = Label(frame, text = "Havent added the rest of the else if statements.")
		b.grid(row = 2, column = 0)

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


clicked = StringVar()
clicked.set(query_options[0])

dropdown = OptionMenu(dropdown_frame, clicked, *query_options, command = select_from_dropdown)
dropdown.grid(row = 1)


# ====================================== Commands 3 - Packing ======================================
# This is an example of why functionalities in the root are unable to use grid, but instead uses
#	pack as it will cause an error where Tkinter's geometry manager grid cannot be used due to
#	already having stuff in the root being managed by some pack(s).

# We cannot use grid here since in the root, there were stuff that we already packed
myButton = Button(root, text="Select From List")
myButton.pack()

footer = Label(root, text = "Created By Group 2 - Chime Nguyen, Ivan Ko, Trung Nguyen",
	  background = "blue", foreground = "white",
	  justify = "center", anchor = "center", padx = 224,
	  pady = 5)
footer.pack(side = "bottom", anchor = "center")

# ============================================== Main ==============================================

root.mainloop()

# ============================================= Credit =============================================

# If we use this feature, we will need to add the following references:
#
# Adding Frames To Your Program - Python Tkinter GUI Tutorial #11
# https://youtu.be/_auZ8TTkojQ
#
# Python | forget_pack() and forget_grid() method in Tkinter by GeeksForGeeks 
# https://www.geeksforgeeks.org/python-forget_pack-and-forget_grid-method-in-tkinter/