import tkinter as tk
from tkinter.filedialog import *
from tkinter import LabelFrame


def save_file():
    new_file = asksaveasfile(mode="w", filetypes=[("text files", ".txt")])
    if new_file is None:
        return
    text = str(body.get("1.0", tk.END))
    new_file.write(text)
    new_file.close()

def open_file():
    file = askopenfile(mode="r", filetypes=[("text files", "*.txt")])
    if file is not None:
        file.seek(0)
        content = file.read()
        body.delete("1.0", tk.END)
        body.insert(tk.INSERT, content)
 
def clear_window():
    body.delete("1.0", tk.END)


lienzo = tk.Tk()
lienzo.geometry("400x400")
lienzo.title("LesNotes")
lienzo.config(bg="black")

head = tk.Frame(lienzo, bg="black")
head.pack(fill= "x", side="top")

border = LabelFrame(lienzo, bd = 6, bg = "black")
border.pack(pady = 10)

b1 = tk.Button(border, text="Open", width=12, bg="#6CD300", fg = "black", command=open_file)
b1.pack(side="left")
b2 = tk.Button(border, text="Save", width=12, bg="#6CD300", fg = "black", command=save_file)
b2.pack(side="left")
b3 = tk.Button(border, text="Clear", width=12, bg="#6CD300", fg = "black", command=clear_window)
b3.pack(side="left")
b4 = tk.Button(border, text="Exit", width=12, bg="#6CD300", fg = "black", command=exit)
b4.pack(side="left")

body = tk.Text(lienzo, wrap="word", bg="black", insertbackground="#6CD300", 
               fg="#6CD300", font=("Cascadia Code", 12))
body.pack(padx=10, pady=5, expand=True, fill="both")

lienzo.mainloop( )
