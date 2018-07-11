from tkinter import *
import time
import datetime

form = Tk()

form.geometry("350x280")
form.title("แสดงเวลาปัจจุบัน")

def timer():
    getTime = datetime.datetime.now().strftime("%H:%M:%S")
    lb2.configure(text=getTime)
    form.after(1000, timer)
    
lb1 = Label(form, text="แสดงเวลา", width=30, height=1, bg="#00ffff", font="consolas 20 ")
lb1.pack()

lb2 = Label(form, width=30, height=1, bg="#00ffff", font="consolas 20 ")
lb2.pack()

timer()

form.mainloop()
