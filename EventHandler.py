from tkinter import *
Window = Tk()
Window.title("Event Handler")
Window.geometry("100x100")
def HandleKeyPress(Event):
    """ Print the character associated to the key pressed! """
    print(Event.char)
Window.bind("<KeyPress>", HandleKeyPress)
def HandleMouseClick(Event):
    print("\n The button was clicked! ")
Button = Button(text = " Click Me! ")
Button.pack()
Button.bind("<Button-1>", HandleMouseClick)
Window.mainloop()