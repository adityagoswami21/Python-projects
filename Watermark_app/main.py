from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

def open_image():
    global img, img_display
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img.thumbnail((400, 400))
    img_display = ImageTk.PhotoImage(img)
    panel.config(image=img_display)





root = Tk()
root.title("Watermark App")

panel = Label(root)
panel.pack()