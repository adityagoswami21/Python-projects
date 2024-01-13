from tkinter import *
import random
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("./data/Italian_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang_display, text="Italian", fill="black")
    canvas.itemconfig(word_display, text=current_card["Italian"], fill="black")
    canvas.itemconfig(card_front, image=my_image_3)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_front, image=card_back)
    canvas.itemconfig(lang_display, text="English", fill="white")
    canvas.itemconfig(word_display, text=current_card["English"], fill="white")


window = Tk()
window.title('Flashcard Game')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


my_image_3 = PhotoImage(file="./images/card_front.png")
canvas = Canvas(width=810, height=530, background=BACKGROUND_COLOR, highlightthickness=0)
card_front = canvas.create_image(410, 270, image=my_image_3)
card_back = PhotoImage(file="./images/card_back.png")

lang_display = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_display = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

my_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=my_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

my_image_2 = PhotoImage(file="./images/right.png")
right_button = Button(image=my_image_2, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)
next_card()


window.mainloop()
