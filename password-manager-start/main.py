from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)

name_entry = Entry(width=35)
name_entry.grid(column=1, row=2, columnspan=2)

pas_entry = Entry(width=21)
pas_entry.grid(column=1, row=3)

gen_button = Button(text="Generate Password")
gen_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
