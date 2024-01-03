from tkinter import *
window = Tk()
window.title("Feet to Cm Converter ")
window.minsize(width=400, height=200)
window.config(padx=40, pady=40)

equal_label = Label(text="is equal to", font=("Arrus BT", 15, "bold"))
equal_label.grid(column=0, row=1)
equal_label.config(pady=10, padx=10)

entry = Entry()
entry.get()
entry.grid(column=1, row=0)

feet_label = Label(text="Feet", font=("Arrus BT", 15, "bold"))
feet_label.grid(column=2, row=0)
feet_label.config(padx=10, pady=10)
window.mainloop()
