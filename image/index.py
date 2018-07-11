from tkinter import *
from PIL import ImageTk, Image

img1 = Image.open("img1.png")
img2 = Image.open("img2.png")
img3 = Image.open("img3.png")
img4 = Image.open("img4.png")
img5 = Image.open("img5.png")

form = Tk()
form.geometry("300x300")
form.title("รูปภาพ")
    
showimg5 = ImageTk.PhotoImage(img5)
showimg4 = ImageTk.PhotoImage(img4)
showimg3 = ImageTk.PhotoImage(img3)
showimg2 = ImageTk.PhotoImage(img2)
showimg1 = ImageTk.PhotoImage(img1)

# i = 0
# def changeImg():
#     global i 
#     i = i + 1
#     if i == 1:
#         lb1.configure(image=showimg4)
#     if i == 2:
#         lb1.configure(image=showimg3)
#     if i == 3:
#         lb1.configure(image=showimg2)
#     if i == 4:
#         lb1.configure(image=showimg1)
#         i =0

# btn1 = Button(form,text="เปลี่ยนภาพ", width=20,height=1,command=changeImg)
# btn1.pack(pady=10)

lb1 = Label(form)
lb1.pack(pady=70)

def image1():
    lb1.configure(image=showimg5)
    form.after(300, image2)

def image2():
    lb1.configure(image=showimg4)
    form.after(300, image3)

def image3():
    lb1.configure(image=showimg3)
    form.after(300, image4)

def image4():
    lb1.configure(image=showimg2)
    form.after(300, image5)

def image5():
    lb1.configure(image=showimg1)
    form.after(300, image1)

image1()

form.mainloop()


