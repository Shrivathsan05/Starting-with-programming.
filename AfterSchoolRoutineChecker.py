from tkinter import *
from tkinter import messagebox
Window = Tk()
Window.title("After School Routine Checker")
Window.geometry("400x300")
AppHeadingLabel = Label(Window, text=" After School Routine Checker ", font=("Arial", 16))
AppHeadingLabel.pack(pady=10)
InstructionLabel = Label(Window, text=" Please enter your after school routine below : ", font=("Arial", 12))
InstructionLabel.pack(pady=5)
EntryWidget = Entry(Window, width=30)
EntryWidget.pack(pady=5)
LastTypedCharacterLabel = Label(Window, text=" Last typed character : ", font=("Arial", 12))
LastTypedCharacterLabel.pack(pady=5)
def CheckLastCharacter(event):
    LastCharacter = EntryWidget.get()[-1] if EntryWidget.get() else ""
    LastTypedCharacterLabel.config(text=f" Last typed character : {LastCharacter}")
def HandleKeyPress(event):
    CheckLastCharacter(event)
def HandleMouseClick(event):
    CheckLastCharacter(event)
def LeftClickDetected(event):
    RoutineMessageLabel.pack(pady=5)
def RightClickDetected(event):
    RoutineMessageLabel.pack_forget()
RoutineMessageLabel = Label(Window, text=" You clicked the Left Mouse Button! ", font=("Arial", 12))
RoutineMessageLabel.pack(pady=5)
Window.bind("<Button-1>", LeftClickDetected)
Window.bind("<Button-3>", RightClickDetected)
def CheckRoutine():
    if EntryWidget.get().strip() == "":
        messagebox.showwarning(" Routine Check ", " Please enter your after school routine! ")
    else:
        messagebox.showinfo(" Routine Check ", f" Your after school routine is : {EntryWidget.get()} ")
CheckRoutineButton = Button(Window, text=" Check Routine ", command=CheckRoutine)
CheckRoutineButton.pack(pady=10)
RoutineMessageLabel.pack_forget()
Window.mainloop()