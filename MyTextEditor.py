from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
Window = Tk()
Window.title("My, (Shrivathsan's), Text Editor")
Window.geometry("600x500")
Window.rowconfigure(0, minsize = 800, weight = 1)
Window.columnconfigure(1, minsize = 800, weight = 1)
def OpenFile():
    """Open a file for editing."""
    FilePath = askopenfilename(filetypes=[(" Text Files ", " *.txt "), (" All Files ", " *.* ")])
    if not FilePath:
        return
    TextEdit.delete(1.0, END)
    with open(FilePath, "r") as InputFile:
        text = InputFile.read()
        TextEdit.insert(END, text)
        InputFile.close()
        Window.title(f" My, (Shrivathsan's), Text Editor - {FilePath}")
def SaveFile():
    FilePath = asksaveasfilename(defaultextension="txt", filetypes=[(" Text Files ", " *.txt "), (" All Files ", " *.* ")])
    if not FilePath:
        return
    with open(FilePath, "w") as OutputFile:
        Text = TextEdit.get(1.0, END)
        OutputFile.write(Text)
    Window.title(f" My, (Shrivathsan's), Text Editor - {FilePath}")
TextEdit = Text(Window)
FrameButtons = Frame(Window, relief=RAISED, bd=2)
ButtonOpen = Button(FrameButtons, text=" Open ", command=OpenFile)
ButtonSave = Button(FrameButtons, text=" Save As... ", command=SaveFile)
ButtonOpen.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
ButtonSave.grid(row=1, column=0, sticky="ew", padx=5)
FrameButtons.grid(row=0, column=0, sticky="ns")
TextEdit.grid(row=0, column=1, sticky="nsew")
Window.mainloop()