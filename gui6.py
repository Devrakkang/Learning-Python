from tkinter import *

form = Tk()
form.geometry("350x280")
form.title("เปลี่ยนสีพื้นหลัง")
lb1 = Label(form, text="change background color",font="angsana 20 bold",width=25)
lb1.pack()

# i = 0
# def timer():
#     global i
#     i = i + 1
#     if i == 1:
#         form.configure(bg="red")
#     if i == 2:
#         form.configure(bg="green")
#     if i == 3:
#         form.configure(bg="blue")
#         i = 0

#     form.after(1000, timer)

def red():
    form.configure(bg="red")
    form.after(1000, yellow)

def yellow():
    form.configure(bg="yellow")
    form.after(1000, green)

def green():
    form.configure(bg="green")
    form.after(1000, red)

red()

form.mainloop()


