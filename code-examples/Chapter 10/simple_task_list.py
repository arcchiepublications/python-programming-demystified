import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a frame for the Entry and Add button
frame_tasks = tk.Frame(root)
frame_tasks.pack()

# Create the entry widget
task_entry = tk.Entry(frame_tasks, width=50)
task_entry.pack(side=tk.LEFT)

# Create the add task button
button_add_task = tk.Button(frame_tasks, text="Add task", command=add_task)
button_add_task.pack(side=tk.LEFT)

# Create the listbox to display tasks
listbox_tasks = tk.Listbox(root, height=10, width=50)
listbox_tasks.pack()

# Create the delete task button
button_delete_task = tk.Button(root, text="Delete task", command=delete_task)
button_delete_task.pack()

# Start the main event loop
root.mainloop()
