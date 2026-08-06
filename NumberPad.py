#Create a visual number pad interface using Tkinter! Students will learn to use nested loops, grid layout management, frames, and labels to build a phone-style number pad with organized rows and columns.
from tkinter import *
Root = Tk()
Root.title("Number Pad")
Root.geometry("250x300")
Numbers = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ["#", 0, "*"]]
for s in range(4) :
    Root.columnconfigure(s, weight=1, minsize=75)
    Root.rowconfigure(s, weight=1, minsize=50)
    for k in range(0, 3) :
        TheFrame = Frame(master=Root, relief=SUNKEN, borderwidth=1)
        TheFrame.grid(row=s, column=k)
        TheLabel =Label(master=TheFrame, text=Numbers[s][k], bg = "#d0efff")
        TheLabel.pack(padx=3, pady=3)
Root.mainloop()