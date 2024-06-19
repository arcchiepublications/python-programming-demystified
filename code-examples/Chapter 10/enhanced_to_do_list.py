import tkinter as tk
from tkinter import messagebox, simpledialog

def add_task():
    task = simpledialog.askstring("Add Task", "Enter a task:")
    if task:
        listbox_tasks.insert(tk.END, task)

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete.")

def about():
    messagebox.showinfo("About", "To-Do List Application\nVersion 1.0")

# Create the main window
root = tk.Tk()
root.title("Enhanced To-Do List")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add menu items
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Add Task", command=add_task)
file_menu.add_command(label="Delete Task", command=delete_task)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Create the listbox to display tasks
listbox_tasks = tk.Listbox(root, height=10, width=50)
listbox_tasks.pack()

# Start the main event loop
root.mainloop()
