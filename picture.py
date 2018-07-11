from tkinter import *
from PIL import ImageTk, Image

img = Image.open("21.jpg")
form = Tk()
form.geometry("600x600")
form.title("รูปภาพ")

# canvas = Canvas(form)
# canvas.pack(pady=10)
# canvas.image = ImageTk.PhotoImage(img)
# canvas.create_image(150,200,image=canvas.image)
showimg = ImageTk.PhotoImage(img)
lb1 = Label(form, image=showimg)
lb1.pack()


form.mainloop()


