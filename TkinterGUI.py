# Install GUI For Python
# -- PyQt5 : pip3 install PyQt5
# -- Tkinter: pip3 install tkinter
# -- Kivy: pip3 install kivy


# Import TKinter
from tkinter import *
import sqlite3

# Create tkinter window
root = Tk()

root.title('Address Book')
root.geometry("400x400")



# Connect to the Library Management System Database and create the tables, if they are not created
conn = sqlite3.connect('library_management_system.db')
add_book_c = conn.cursor()



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


# Add Tables Into DB Via Python
# add_book_c.execute('''CREATE TABLE ADDRESSES(FIRST_NAME TEXT,
# 					LAST_NAME TEXT,
# 					ADDRESS TEXT,
# 					CITY TEXT,
# 					STATE TEXT,
# 					ZIPCODE INT)
# 	''')



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
# f_name_label = Label(root, text ='First Name: ')
# f_name_label.grid(row = 0, column = 0)

# l_name_label = Label(root, text = 'Last Name: ')
# l_name_label.grid(row = 1, column = 0)

# street_label = Label(root, text = 'Street: ')
# street_label.grid(row = 2, column = 0)

# city_label = Label(root, text = 'City: ')
# city_label.grid(row = 3, column = 0, sticky = "w")

# state_label = Label(root, text = 'State: ')
# state_label.grid(row = 4, column = 0)

# zcode_label = Label(root, text = 'Zipcode: ')
# zcode_label.grid(row = 5, column = 0)



# Create buttons to access DB
# submit_btn = Button(root, text = "Add Address", command = submit)
# submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# input_query_btn = Button(root, text = "Show Records", command = input_query)
# input_query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)



# Run Main Loop
root.mainloop()