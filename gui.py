import tkinter as tk

# Form--------------------------------------------------------------------------------------------------------

gui = tk.Tk()
message = tk.StringVar()

gui.geometry("800x500")
gui.title("Test")
gui.configure(background="lightblue")

def btnClick():
    msg = "Hello"
    msg += str(tb1.get('1.0','end-1c'))
    message.set(msg)
    gui.update()

# Component
lb2 = tk.Label(gui, text="Python Gui Tkinter", fg="green", bg ="pink", font="angsana 25 bold",width=50).pack(pady=10)
tb1 = tk.Text(width=33,height=1,font="angsana 15 bold").pack(pady=10)
btn1 = tk.Button(text="Click Me",fg="blue",bg="white",font="angsana 15 bold",width=30,command=btnClick).pack(pady=10)
# btn2 = tk.Button(text="Exit",fg="red",bg="black",font="angsana 15 bold",width=30,command=gui.destroy).pack(pady=10)
lb2 = tk.Label(gui, textvariable=message, fg="green", bg ="yellow", font="angsana 25 bold",width=18).pack(pady=10)


# loop
gui.mainloop()

#End Form-----------------------------------------------------------------------------------------------------------
