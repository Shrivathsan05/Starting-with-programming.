from tkinter import *
from tkinter import messagebox
Root = Tk()
Root.geometry("200x200")
def MessageBox():
    messagebox.showwarning(" Alert! Virus Detected! ", " Stop! A virus has been detected on your system! ")
Button = Button(Root, text = " Scan For Viruses! ", command = MessageBox)
Button.place(x = 40, y = 80)
Root.mainloop()