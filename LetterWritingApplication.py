from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
Window = Tk()
Window.title("Letter Writing Application")
Window.geometry("800x600")
Window.grid_rowconfigure(0,minsize=500, weight=1)
Window.grid_columnconfigure(0,minsize=500, weight=1)
def OpenLetter():
    file_path = askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return
    with open(file_path, "r") as input_file:
        text = input_file.read()
        text_area.delete(1.0, END)
        text_area.insert(END, text)
    Window.title(f"Letter Writing Application - {file_path}")
def SaveLetter():
    file_path = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return
    with open(file_path, "w") as output_file:
        text = text_area.get(1.0, END)
        output_file.write(text)
    Window.title(f"Letter Writing Application - {file_path}")
    print("Letter saved successfully!")
text_area = Text(Window)
text_area.grid(row=0, column=0, sticky="nsew")
fr_buttons = Frame(Window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text=" Open A Letter! ", command=OpenLetter)
btn_saveas = Button(fr_buttons, text=" Save As Another Letter! ", command=SaveLetter)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_saveas.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
fr_buttons.grid(row=0, column=1, sticky="n")
text_area.focus()
Window.mainloop()