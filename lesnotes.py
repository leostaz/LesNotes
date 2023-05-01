import tkinter as tk
from tkinter.filedialog import *
from tkinter import LabelFrame


current_file = None

def save_file():
    global current_file
    if current_file is None:
        new_file = asksaveasfile(mode="w", filetypes=[("All files", "*.*"), 
                                                      ("Text files", "*.txt"), 
                                                      ("Python files", "*.py")])
        if new_file is None:
            return
        current_file = new_file.name

    text = str(body.get("1.0", tk.END))
    with open(current_file, 'w') as f:
        f.write(text)

def open_file():
    file = askopenfile(mode="r", filetypes=[("All files", "*.*"), 
                                            ("Text files", "*.txt"),
                                            ("Python files", "*.py")])
    if file is not None:
        file.seek(0)
        content = file.read()
        body.delete("1.0", tk.END)
        body.insert(tk.INSERT, content)
 
def clear_window():
    body.delete("1.0", tk.END)


lienzo = tk.Tk()
lienzo.geometry("800x600")
lienzo.title("LesNotes")
lienzo.config(bg="black")

head = tk.Frame(lienzo, bg="black")
head.pack(fill= "x", side="top")

border = LabelFrame(lienzo, bd = 6, bg = "black")
border.pack(pady = 10)

b1 = tk.Button(border, text="Open", width=15, bg="#6CD300", fg = "black", 
               font=("Cascadia Code", 10, "bold"), command=open_file)
b1.pack(side="left")
b2 = tk.Button(border, text="Save", width=15, bg="#6CD300", fg = "black", 
               font=("Cascadia Code", 10, "bold"), command=save_file)
b2.pack(side="left")
b3 = tk.Button(border, text="Clear", width=15, bg="#6CD300", fg = "black", 
               font=("Cascadia Code", 10, "bold"), command=clear_window)
b3.pack(side="left")
b4 = tk.Button(border, text="Exit", width=15, bg="#6CD300", fg = "black", 
               font=("Cascadia Code", 10, "bold"), command=exit)
b4.pack(side="left")

body = tk.Text(lienzo, wrap="word", bg="black", insertbackground="#6CD300", 
               fg="#6CD300", font=("Cascadia Code", 12))
body.pack(padx=10, pady=5, expand=True, fill="both")

lienzo.mainloop( )
