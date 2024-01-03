from tkinter import *
window = Tk()
window.title("Feet to Cm Converter ")
window.minsize(width=400, height=200)
window.config(padx=40, pady=40)

equal_label = Label(text="is equal to", font=("Arrus BT", 15, "bold"))
equal_label.grid(column=0, row=1)
equal_label.config(pady=10, padx=10)

entry = Entry()
print(entry.get())
entry.grid(column=1, row=0)

feet_label = Label(text="Feet", font=("Arrus BT", 15, "bold"))
feet_label.grid(column=2, row=0)
feet_label.config(padx=10, pady=10)

con_dig = Label(text="0", font=("Arrus BT", 15, "bold"))
con_dig.grid(column=1, row=1)

Cm_label = Label(text="Cm", font=("Arrus BT", 15, "bold"))
Cm_label.grid(column=2, row=1)


def conversion():
    try:
        num = float(entry.get())
        cm_value = num * 30.48
        con_dig['text'] = f"{cm_value:.2f}"
    except ValueError:
        con_dig['text'] = f"{con_dig:.2f}"


calc_button = Button(text="Calculate",command=conversion, font=("Arrus BT", 15, "bold"))
calc_button.grid(column=1, row=2)

window.mainloop()
