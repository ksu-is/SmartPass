# Python program to generate random 
# password using Tkinter module 
import random 
from tkinter import *
from tkinter.ttk import *

# Function for calculation of password 
def low(): 
	entry.delete(0, END) 

	# Get the length of passowrd 
	length = var1.get() 

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = "" 

	# if strength selected is low 
	if var.get() == 1: 
		for i in range(0, length): 
			password = password + random.choice(lower) 
		return password 

	# if strength selected is medium 
	elif var.get() == 0: 
		for i in range(0, length): 
			password = password + random.choice(upper) 
		return password 

	# if strength selected is strong 
	elif var.get() == 3: 
		for i in range(0, length): 
			password = password + random.choice(digits) 
		return password 
	else: 
		print("Please choose an option") 


# Function for generation of password 
def generate(): 
	password1 = low() 
	entry.insert(10, password1) 


# Function for clearing generated password 
def clear_text(): 
	entry.delete(0, END)



# Main Function 

# create GUI window 
root = Tk() 
var = IntVar() 
var1 = IntVar() 

# Title of your GUI window 
root.title("Welcome to SmartPass!") 

# create label and entry to show 
# password generated 
Random_password = Label(root, text="Password") 
Random_password.grid(row=0) 
entry = Entry(root) 
entry.grid(row=1) 

# create label for length of password 
combo_label = Label(root, text="Length") 
combo_label.grid(row=2) 

# Combo Box for length of your password 
combo = Combobox(root, textvariable=var1) 
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
				17, 18, 19, 20, 21, 22, 23, 24, 25, 
				26, 27, 28, 29, 30, 31, 32, "Length") 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(row=3) 

# create Buttons Clear which will Clear 
# Generate which will generate the password 
clear_button = Button(root, text="Clear", command=clear_text) 
clear_button.grid(row=9) 
generate_button = Button(root, text="Generate", command=generate) 
generate_button.grid(row=8) 

# Radio Buttons for deciding the 
# strength of password 
# Default strength is Medium 
strength_label = Label(root, text="Password Strength")
strength_label.grid(row=4)
radio_low = Radiobutton(root, text="Low", variable=var, value=1) 
radio_low.grid(row=5, sticky='W') 
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0) 
radio_middle.grid(row=6, sticky='W') 
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3) 
radio_strong.grid(row=7, sticky='W') 



# specify the GUI window dimensions
root.geometry("230x300")

# start the GUI 
root.mainloop() 
