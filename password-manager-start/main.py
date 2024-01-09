import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = [random.choice(letters) for _ in range(nr_letters)]
password_list += [random.choice(symbols) for _ in range(nr_symbols)]
password_list += [random.choice(numbers) for _ in range(nr_numbers)]

random.shuffle(password_list)

password = "".join(password_list)

print(f"Your password is: {password}")


def password_generator():
    pas_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def find_password():
    website = web_entry.get()
    try:
        with open("data.json", 'r') as doc_file:
            n = json.load(doc_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="No Data File Found.")
    else:
        if website in n:
            messagebox.showinfo(title="Your Password", message=f"website's name: {website}\n "
                                                               f"Password: {n[website]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")


def save():
    website = web_entry.get()
    name = name_entry.get()
    password = pas_entry.get()
    new_data = {
        website: {
            'email': name,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!", message="Please fill the information!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"following are the details:\nEmail:{name}"f"\nPassword:"
                                                              f" {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open('data.json', 'r') as data:
                    content = json.load(data)
            except FileNotFoundError:
                with open('data.json', 'w') as data:
                    json.dump(new_data, data, indent=4)
            else:
                content.update(new_data)
                with open('data.json', 'w') as data:
                    json.dump(content, data, indent=4)
            finally:
                web_entry.delete(0, END)
                name_entry.delete(0, END)
                pas_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.minsize(width=500, height=400)
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img, )
canvas.grid(column=1, row=0, columnspan=2)

website_txt = Label(text="Website:")
website_txt.config(pady=10, padx=10)
website_txt.grid(column=0, row=1)

name_txt = Label(text="Email/Username:")
name_txt.config(pady=10, padx=10)
name_txt.grid(column=0, row=2)

pas_txt = Label(text="Password:")
pas_txt.config(pady=10, padx=10)
pas_txt.grid(column=0, row=3)

web_entry = Entry(width=21)
web_entry.grid(row=1, column=1)

name_entry = Entry(width=35)
name_entry.grid(column=1, row=2, columnspan=2)
name_entry.insert(0, 'adityagoswami193@gmail.com')

pas_entry = Entry(width=21)
pas_entry.grid(column=1, row=3)

gen_button = Button(text="Generate Password", command=password_generator)
gen_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()
