# Project Name - Password Generator
# Developed By - Ajay Thakur (2016kuec2026@iiitkota.ac.in)
# Branch Name - Electronics and Communication Engineering
# Institute Name - Indian Institute of Information Technology Kota (An Institute of National Importance under an Act of Parliament)
# Submitted To -  Code Alpha
# Project Link (GitHub) - https://github.com/ajaythakur3369/CodeAlpha-Password-Generator/blob/main/Task_1_Password_Generator.py  

# Project Summery - The most difficult part of managing multiple accounts is generating a difficult strong password for each. A strong password is a mix of alphabets, 
# numbers, and alphanumeric characters. Therefore, the best use of Python could be building a project where you could generate random passwords for any of your accounts.
# In order to create a strong password, users can use this password generator to generate a random and customized password. 

# Imported required modules for the progarm
import tkinter as tk
import string
import random
from tkinter import messagebox

# Create a tkinter window
root = tk.Tk()

# Set the geometry (widthxheight)
root.geometry('544x335')
root.minsize(400, 250)

# root window title
root.title("Password Generator")

# Widgets
# Creating a label
heading = tk.Label(root, text = "Password Generator", font = ("Georgia", 20, "bold"))
heading.pack(pady = 30)

# The label for the length of the password
label = tk.Label(root, text = "Enter the length of the password", font = ("Georgia", 11))
label.pack(pady = 15)

# Creating an entry for the length of the password
entry = tk.Entry(root, width = 10)
entry.pack()

# Function to generate a strong password with specified length
def generateStrongPassword(length):

    # Uppercase letters
    upper = string.ascii_uppercase 

    # Lowercase letters   
    lower = string.ascii_lowercase 

    # Numerical digits    
    digits = string.digits    

    # Punctuation symbols         
    symbols = string.punctuation       

    # Password contains atleast one character from each character set
    pw = [random.choice(upper), random.choice(lower), random.choice(digits), random.choice(symbols)]
    
    remainingLength = length - 4
    characters_list = list(upper + lower + digits + symbols)

    # Extend the pw list with random characters from characters_list
    for i in range(remainingLength):
        pw.extend(random.choice(characters_list))

    return "".join(pw)

# Function to create the onclick event for generating the password
def onClick():
    len = entry.get()
    if len == '':
         
        # Display error message in case of an empty input
         messagebox.showerror('Error', 'Please provide an input')
    else:
        try:
            length = int(len)
            if length < 8:

                # Display a warning if the password length is too short
                messagebox.showwarning('Warning','Minimum length of the password should be 8')
            else:
                password = generateStrongPassword(length)
                msg = "Password is : " + password
                label.configure(text = msg)

                # Hiding the input field and button
                entry.pack_forget()
                button.pack_forget()

                # Display the new button with added padding
                newButton.pack(pady = 10)
                
        except:
            # Display an error message if the input is not a number i.e a string or a character
            messagebox.showerror('Error', 'Invalid input! Please enter a valid number')

# Creating button
button = tk.Button(root, text = "Generate", foreground = "blue", command = onClick)
button.pack(pady = 4)

newButton = tk.Button(root, text = "Generate another password", foreground = "blue", command = onClick)

# Execute Tkinter
root.mainloop()