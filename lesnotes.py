import tkinter as tk
from tkinter.filedialog import *


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

b1 = tk.Button(lienzo, text="Open", bg="green", command=open_file)
b1.pack(in_=head, side="left")
b2 = tk.Button(lienzo, text="Save", bg="green", command=save_file)
b2.pack(in_=head, side="left")
b3 = tk.Button(lienzo, text="Clear", bg="green", command=clear_window)
b3.pack(in_=head, side="left")
b4 = tk.Button(lienzo, text="Exit", bg="green", command=exit)
b4.pack(in_=head, side="left")

body = tk.Text(lienzo, wrap="word", bg="black", insertbackground='green', fg="green", font=("campbell", 14))
body.pack(padx=10, pady=5, expand=True, fill="both")

lienzo.mainloop( )
