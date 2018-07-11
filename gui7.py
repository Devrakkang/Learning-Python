from tkinter import*
import sys

gui1 = Tk()
gui2 = Tk()

def bt1_Click():
      gui2.deiconify()
      gui1.withdraw()
def bt3_Click():
      gui1.deiconify()
      gui2.withdraw()

def exit():
    gui1.destroy()
    gui2.destroy()
    sys.exit()

gui1.geometry("300x250")
gui1.title("form1")
gui1.configure(bg="pink")

bt1 = Button(gui1,text="Show form2",width=20,height=1,command=bt1_Click)
bt1.pack(pady = 50)

bt2 = Button(gui1,text="exit",command=exit)
bt2.pack()


gui2.geometry("300x250")
gui2.title("form2")
gui2.configure(bg="yellow")
gui2.withdraw()

bt3 = Button(gui2,text="Show form1",width=20,height=1,command=bt3_Click)
bt3.pack(pady = 50)

bt4 = Button(gui2,text="exit",command=exit)
bt4.pack()


gui1.mainloop()
gui2.mainloop()
