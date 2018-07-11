from tkinter import *

gui = Tk()
ans = StringVar()

gui.geometry("350x350")
gui.title("โปรแกรมบวกเลข")
gui.configure(background="#ff8040")

def click():
    ans.set(int(tb1.get('1.0','end-1c'))+int(tb2.get('1.0','end-1c')))
    gui.update()
    
lb1 = Label(gui, text="Input Number1 : ",width=20,height=1,background="red",font="colsolas 15")
lb1.pack(pady=10)

tb1 = Text(gui,width=20,height=1,font="colsolas 15")
tb1.pack(pady=10)

lb2 = Label(gui, text="Input Number2 : ",width=20,height=1,background="red",font="colsolas 15")
lb2.pack(pady=10)

tb2 = Text(gui,width=20,height=1,font="colsolas 15")
tb2.pack(pady=10)

btn1 = Button(gui, text="OK", width=20, height=1,command=click,font="colsolas 15")
btn1.pack(pady=10)

lb2 = Label(gui, textvariable=ans,width=20,height=1,background="#ff8040",font="colsolas 20")
lb2.pack(pady=10)

gui.mainloop()