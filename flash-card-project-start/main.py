from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title('Flashcard Game')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

my_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=my_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)

my_image_2 = PhotoImage(file="./images/right.png")
right_button = Button(image=my_image_2, highlightthickness=0)
right_button.grid(column=1, row=1)

my_image_3 = PhotoImage(file="./images/card_front.png")
canvas = Canvas(width=810, height=530, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(410, 270, image=my_image_3)
canvas.create_text(400, 150, text="Italian", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
window.mainloop()
