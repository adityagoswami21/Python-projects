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

def add_watermark():
    global img
    watermark = Image.open("watermark.png").convert("RGBA")
    watermark = watermark.resize((100, 100))
    img = img.convert("RGBA")
    img.paste(watermark, (10, 10), watermark)

    preview = ImageTk.PhotoImage(img)
    panel.config(image=preview)
    panel.image = preview

def save_image():
    img.convert("RGB").save("watermarked_image.jpg")

root = Tk()
root.title("Watermark App")

panel = Label(root)
panel.pack()

Button(root, text="Open Image", command=open_image).pack()
Button(root, text="Add Watermark", command=add_watermark).pack()
Button(root, text="Save Image", command=save_image).pack()

root.mainloop()