#Create an interactive GUI application using Tkinter that greets users by name and displays today's date! Students will learn to build windows, add widgets, handle button clicks, and display dynamic messages in a text box.
from tkinter import *
from datetime import date
Root = Tk()
Root.title(" Get Started with Widgets ")
Root.geometry("400x300")
label = Label(text = " Hey There!", fg = "White", bg = "#072F5F", height = 1, width = 300)
NameLabel = Label(text = " Full Name ", bg = "#3895D3")
NameEntry = Entry()
def DisplayMessage():
    Name = NameEntry.get()
    global Message
    Message = " Welcome To The Application! \n Today's date is : "
    Greet = "Hello, " + Name + "!\n "
    text_box.insert(END, Greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())
text_box = Text( height = 3 )
Button = Button(text = " Begin! ", command = DisplayMessage, height = 1, bg = "#1261A0", fg = "White")
label.pack()
NameLabel.pack()
NameEntry.pack()
Button.pack()
text_box.pack()
Root.mainloop()