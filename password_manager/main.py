import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def gen_pass():
    password_entry.delete(0,"end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 6)
    nr_numbers = randint(2, 6)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_symbols + password_letters + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website:{
        "email":email,
        "password":password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message = "Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data,data_file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")

def search_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

# Canvas for lock
canvas = tk.Canvas(width=200,height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = tk.Label(text="Password:")
password_label.grid(row=3,column=0)

# Entries
website_entry = tk.Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry = tk.Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"yoshijoshio@gmail.com")
password_entry = tk.Entry(width=21)
password_entry.grid(row=3,column=1)

# Buttons
gen_pass_button = tk.Button(text="Generate Password",command=gen_pass)
gen_pass_button.grid(row=3,column=2)
add_button = tk.Button(text="Add",width=36,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)
search_button = tk.Button(text="Search",width=15, command=search_password)
search_button.grid(row=1,column=2)

window.mainloop()