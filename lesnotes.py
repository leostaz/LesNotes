import tkinter as tk
from tkinter.filedialog import *
from tkinter import LabelFrame, messagebox


current_file = None

def open_file(event=None):
    global current_file

    file = askopenfile(mode="r", filetypes=[("All files", "*.*"), 
                                            ("Text files", "*.txt"),
                                            ("Python files", "*.py")])
    if file is not None:
        file.seek(0)
        content = file.read()
        body.delete("1.0", tk.END)
        body.insert(tk.INSERT, content)
        current_file = file.name
 
def close_file(event=None):
    global current_file

    if current_file:
        response = messagebox.askyesnocancel("Close", "Save changes before closing?")

        if response:
            save_file()
            body.delete("1.0", tk.END)
            current_file = None

        elif response is False:
            body.delete("1.0", tk.END)
            current_file = None

        else:
            return

def save_file(event=None):
    global current_file

    if current_file is None:
        new_file = asksaveasfile(mode="w", filetypes=[("All files", "*.*"), 
                                                      ("Text files", "*.txt"), 
                                                      ("Python files", "*.py")])
        if new_file is None:
            return
        current_file = new_file.name

    else:
        new_file = open(current_file, mode="w")

    text = str(body.get("1.0", tk.END))
    new_file.write(text)
    new_file.close()

def clear_window(event=None):
    body.delete("1.0", tk.END)

def exit_app(event=None):
    global current_file

    if current_file:
        response = messagebox.askyesnocancel("Exit", "Save changes?")

        if response:
            save_file()
            lienzo.destroy()

        elif response is False:
            lienzo.destroy()
        
        else:
            return

    else:
        lienzo.destroy()

def undo(event=None):
    global current_file

    if current_file is True:
        if body.edit_modified():
            body.edit_undo()

def redo(event=None):
    global current_file
    
    if current_file is True:
        if body.edit_modified():
            body.edit_redo()

def copy_text():
    body.clipboard_clear()
    selected_text = body.get(tk.SEL_FIRST, tk.SEL_LAST)
    body.clipboard_append(selected_text)

def cut_text():
    copy_text()
    body.delete(tk.SEL_FIRST, tk.SEL_LAST)

def paste_text():
    text_to_paste = body.clipboard_get()
    body.insert(tk.INSERT, text_to_paste)


lienzo = tk.Tk()
lienzo.geometry("800x600")
lienzo.title("LesNotes")
lienzo.config(bg="black")

head = tk.Frame(lienzo, bg="black")
head.pack(fill="x", side="top")

border = LabelFrame(lienzo, bd=6, bg="black")
border.pack(pady=10)

b1 = tk.Button(border, text="Open", width=15, bg="#00FF00", fg="black", 
               font=("Cascadia Code", 12, "bold"), command=open_file)
b1.pack(side="left")
b2 = tk.Button(border, text="Close", width=15, bg="#00FF00", fg="black", 
               font=("Cascadia Code", 12, "bold"), command=close_file)
b2.pack(side="left")
b3 = tk.Button(border, text="Save", width=15, bg="#00FF00", fg="black", 
               font=("Cascadia Code", 12, "bold"), command=save_file)
b3.pack(side="left")
b4 = tk.Button(border, text="Clear", width=15, bg="#00FF00", fg="black", 
               font=("Cascadia Code", 12, "bold"), command=clear_window)
b4.pack(side="left")
b5 = tk.Button(border, text="Exit", width=15, bg="#00FF00", fg="black", 
               font=("Cascadia Code", 12, "bold"), command=exit_app)
b5.pack(side="left")

body = tk.Text(
                lienzo, 
                wrap="word", 
                bg="black", 
                insertbackground="#00FF00",
                selectbackground="#00FF00", 
                selectforeground="black",
                fg="#00FF00", 
                font=("Cascadia Code", 12),
                undo=True
                )
body.pack(
            padx=10, 
            pady=5, 
            expand=True, 
            fill="both"
            )

body.configure(
                highlightthickness=2, 
                highlightbackground="#00FF00", 
                highlightcolor="#00FF00"
                )

lienzo.bind("<Control-o>", open_file)
lienzo.bind("<Control-C>", close_file)
lienzo.bind("<Control-s>", save_file) 
lienzo.bind("<Control-d>", clear_window)
lienzo.bind("<Control-q>", exit_app)
lienzo.bind("<Control-z>", undo)
lienzo.bind("<Control-y>", redo)
lienzo.bind("<Control-c>", copy_text)
lienzo.bind("<Control-x>", cut_text)
lienzo.bind("<Control-v>", paste_text)

lienzo.mainloop()
