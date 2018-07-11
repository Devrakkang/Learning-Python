from tkinter import*

gui = Tk()
message = StringVar()

gui.geometry("300x300")
gui.title("Event Click")
gui.configure(background="blue")

def Click():
    msg = "Hello"
    msg += str(tb1.get('1.0','end-1c'))
    message.set(msg)
    gui.update()

lb1 = Label(gui, text="Input Your Name : ", width=20, height=1, background="red")
lb1.pack(pady=10)

tb1 = Text(gui, width=18, height=1)
tb1.pack(pady=10)

bt1 = Button(gui, text="OK", command=Click)
bt1.pack(pady=10)

lb2 = Label(gui, textvariable=message, width=20, height=1)
b.pack(pady=10)

gui.mainloop()