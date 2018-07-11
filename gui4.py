from tkinter import *

gui = Tk()

gui.geometry("350x280")
gui.title("โปรแกรมเปลี่ยนสีพื้นหลังฟอร์ม")

def red():
    gui.configure(bg="red")
    btnRed.configure(bg="red")

def green():
    gui.configure(bg="green")
    btnGreen.configure(bg="green")

def blue():
    gui.configure(bg="blue")
    btnBlue.configure(bg="blue")
    

lb1 = Label(gui, text="กดปุ่มเพื่อเปลี่ยนสีพื้นหลัง",width=30,height=1,bg="#00ffff",font="consolas 20 ").pack()

btnRed = Button(gui, text="Red",width=20,height=2,bg="#000",fg="#fff",command=red)
btnRed.pack(pady=10)

btnGreen = Button(gui, text="Green",width=20,height=2,bg="#000",fg="#fff",command=green)
btnGreen.pack(pady=10)

btnBlue = Button(gui, text="Blue",width=20,height=2,bg="#000",fg="#fff",command=blue)
btnBlue.pack(pady=10)

gui.mainloop()