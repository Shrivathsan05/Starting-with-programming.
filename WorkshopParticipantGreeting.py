from tkinter import *
root = Tk()
root.geometry("400x200")
TitleLabel = Label(root, text=f" Workshop Welcome Desk ")
TitleLabel.pack()
ParticipantNameLabel = Label(root, text=" Participant's Name : ")
ParticipantNameLabel.pack()
ParticipantNameEntry = Entry(root)
ParticipantNameEntry.pack()
GreetingMessage = Label(root, text="Welcome To The Workshop!")
GreetingMessage.pack()
def DisplayGreeting():
    Name = ParticipantNameEntry.get()
    if Name.strip() == "":
        GreetingMessage.configure(text="Please enter your name.", fg="red")
    else:
        GreetingMessage.configure(text=f"Hello, {Name}! Welcome To The Workshop!", fg="green")
def ClearGreeting():
    GreetingMessage.configure(text="_______________", fg="black")
    ParticipantNameEntry.delete(0, END)
DisplayButton = Button(root,text=" Display Greeting ", command=DisplayGreeting)
DisplayButton.place(x = 100, y = 120)
ClearButton = Button(root, text=" Clear Greeting ", command=ClearGreeting)
ClearButton.place(x = 200, y = 120)
root.mainloop()