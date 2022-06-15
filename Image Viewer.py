
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import os

root = Tk()
root.geometry("600x600")
root.title("Image Viewer")
root.config(background="blwhiteue")

label_image = Label(root, bg="white", fg="black", highlightthickness = "5")
label_image.place(relx=0.5, rely=0.5, anchor=CENTER)

image_path = ""

def open_file():
    global image_path
    img_path = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image files","*.jpg;*.gif;*.jpg;;*.png;*.txt")])
    print(img_path)
    img_e = ImageTk.PhotoImage(Image.open(img_path))
    img = img_e
    label_image["image"] = img_e
    img_e.close()
    
button = Button(root,text = "Open an image",command = open_file,bg = "white",fg = "black")
button.place(relx = 0.5,rely = 0.7,anchor = CENTER)

root.mainloop()














