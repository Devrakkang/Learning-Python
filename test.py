#----- ตัวอย่างที่ 29 -----
#------ python Basic GUI-------


from tkinter import*

gui = Tk()
message = StringVar()

def Click():
    message.set("HELLO")
    gui.update()

gui.geometry("350x200")
gui.title("ทดสอบ")
gui.configure(background="blue")

def Click():
    msg = "HELLO"
    msg += str(tb1.get('1.0','end-1c')) #ลบ1ตัว อักษร
    message.set(msg)
    gui.update()

lb1 =Label(gui,text="กรุณากรอกชื่อ", width=20,height=1,background="yellow")
lb1.pack(pady=5)

tb1= Text(gui,width=18,height=1)
tb1.pack(pady=5)

bt1= Button(gui,text="OK",font="angsana 10 bold",command=Click)
bt1.pack(pady=5)

lb2 =Label(gui,textvariable=message,width=20,height=1,background="pink")
lb2.pack(pady=5)


gui.mainloop()
