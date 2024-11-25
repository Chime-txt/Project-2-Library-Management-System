# Import TKinter
from tkinter import *
import sqlite3

# Create tkinter window
root = Tk()
root.title('Library Management System')
root.geometry("600x400")
root.minsize(600, 250)
root.maxsize(600, 800)

# Create frame for the Title only
title_frame = LabelFrame(root, borderwidth = 0, pady = 5)
title_frame.grid(row = 0, columnspan = 10)

# Place title of database system at the top using the frame
title = Label(title_frame, text = "Library Management System",
	  background = "blue", foreground = "white",
	  justify = "center", anchor = "center", padx = 224,
	  pady = 5)
title.pack(side = "top", anchor = "center")



# Define labels
f_name_label = Label(root, text ='First Name: ')
f_name_label.grid(row = 1, column = 0)

l_name_label = Label(root, text ='Last Name: ')
l_name_label.grid(row = 2, column = 1)

address_label = Label(root, text ='Address: ')
address_label.grid(row = 3, column = 2)

street_label = Label(root, text = 'Street: ')
street_label.grid(row = 4, column = 3)

city_label = Label(root, text = 'City: ')
city_label.grid(row = 5, column = 4, sticky = "w")

state_label = Label(root, text = 'State: ')
state_label.grid(row = 6, column = 5)

zcode_label = Label(root, text = 'Zipcode: ')
zcode_label.grid(row = 7, column = 6)



# Run Main Loop
root.mainloop()