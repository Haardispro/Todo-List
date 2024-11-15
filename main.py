from tkinter import *
import sqlite3

w = Tk()
w.title("Todo List")
w.configure(bg="#1e1e1e")
w.resizable(height=False, width=False)

#Fonts
#Heading font
f1 = ('Agave', 25, 'bold')
f2 = ('Agave', 15, 'bold')

# Warning
def warning():
    x = Tk()
    x.title("Warning")
    x.configure(bg="red")
    x.resizable(height=False, width=False)
    Label(x, text="No task entered!", font=f1, fg="white", bg="red") .grid(row=0, column=0, padx=20, pady=20)
 

#Button Functions
def add():
    w = enter.get()
    enter.delete(0, END)
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    if (w == ""):
        warning()
    else:
        listbox.insert(END, "- " + w)
        try:
            cur.execute("CREATE TABLE todo(Task text)")
            cur.execute("INSERT INTO todo VALUES (?)", (w,))
        except sqlite3.OperationalError:
            cur.execute("INSERT INTO todo VALUES (?)", (w,))
    con.commit()
    con.close()

def remove(): 
    selected = listbox.get(ACTIVE)
    x = selected[2:len(selected)]
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    try:
        cur.execute("DELETE FROM todo WHERE Task = (?)", (x,))
    except sqlite3.OperationalError:
        warning()
    con.commit()
    con.close()
    listbox.delete(ACTIVE)

def show():
    listbox.delete(0, END)     
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    try:
        for row in cur.execute("SELECT * FROM todo"):
            listbox.insert(END, "- " + row[0])
    except sqlite3.OperationalError:
        warning()
    con.commit()
    con.close()
    
#Heading
head = Label(w, text="Todo List", font=f1, bg="#1e1e1e", fg="white")
#Listbox
list_head = Label(w, text="Your Tasks:", font=f2, fg="white", bg="#1e1e1e")
listbox = Listbox(w, height = 10,
                  width = 25,
                  bg = "white",
                  activestyle = 'dotbox',
                  font = f1,
                  fg = "#1e1e1e")

#scrollbar
sb = Scrollbar(w,orient="vertical")

listbox.config(yscrollcommand=sb.set)
sb.config(command=listbox.yview)

#Button and Entry
remove = Button(w, text="Remove task", font=f1, command=remove)
add = Button(w, text="Add task", font=f1, command=add)
show = Button(w, text="Show Tasks", font=f1, command=show)
enter_lab = Label(w, text="Enter a task:", font=f2, fg="white", bg="#1e1e1e")
enter = Entry(w, width=25, fg="#1e1e1e", bg="white", font=f1)

#Positions
head.grid(row=0, column=0, padx=20, pady=10)
list_head.grid(row=1, column=0, padx=20, pady=10)
listbox.grid(row=2, column=0, padx=20, pady=10)
enter_lab.grid(row=3, column=0, padx=20, pady=10)
enter.grid(row=4, column=0, padx=20, pady=10)
add.grid(row=5, column=0, padx=20, pady=10)
remove.grid(row=6, column=0, padx=20, pady=10)
show.grid(row=7, column=0, padx=20, pady=10)
sb.grid(row=2, column=1, sticky="ns")

w.mainloop()
