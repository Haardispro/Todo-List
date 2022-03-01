from tkinter import *
from tkinter import messagebox
import keyboard

w = Tk()
w.title("Todo list")
w.resizable(height=False, width=False)
w.config(bg="#282828")

#commands
def add_task():
    task = entry.get()
    if task != "":
        lb.insert(END, task)
        entry.delete(0, END)

    else:
        messagebox.showwarning("warning", "Please enter some task.")

def delete_task():
    lb.delete(ANCHOR)


heading = Label(w, text="Todo List", font=("Cascadia Code", 18), fg="white", bg="#282828")
lb = Listbox(
    w,
    width=25,
    height=8,
    font=('Cascadia Code', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    borderwidth=5
    )   

scrollbar = Scrollbar(w, orient="vertical")
scrollbar.config(command=lb.yview)
scrollbar.grid(row=1, column=1, sticky='ns')
lb.config(yscrollcommand=scrollbar.set)

entry = Entry(w, width=25, font=("Cascadia Code", 18), borderwidth=5)
add_button = Button(w, text="Add Task", width=10, font=("Cascadia Code", 18), borderwidth=5, command=add_task, bg="green", fg="white")
delete_button = Button(w, text="Delete Task", font=("Cascadia Code", 18), borderwidth=5, command=delete_task, bg="red", fg="white")


#positions
heading.grid(row=0, column=0, padx=10, pady=10)
lb.grid(row=1, column=0, padx=10, pady=10)
entry.grid(row=2, column=0, padx=10, pady=10)
add_button.grid(row=3, column=0, padx=10, pady=10)
delete_button.grid(row=4, column=0, padx=10, pady=10)


w.mainloop()
