import tkinter as tk
from tkinter import filedialog, messagebox
import os

def open_directory():
    path = filedialog.askdirectory()
    if path:
        list_files(path)

def list_files(path):
    listbox_files.delete(0, tk.END)
    try:
        for file in os.listdir(path):
            listbox_files.insert(tk.END, file)
    except PermissionError:
        messagebox.showerror("Error", "Permission Denied")

def on_file_select(event):
    index = listbox_files.curselection()[0]
    selected_file = listbox_files.get(index)
    label_file_info.config(text=f"Selected File: {selected_file}")

# Create the main window
root = tk.Tk()
root.title("Simple File Explorer")

# Create a button to open directory
button_open_directory = tk.Button(root, text="Open Directory", command=open_directory)
button_open_directory.pack()

# Create a listbox to display files
listbox_files = tk.Listbox(root, height=15, width=50)
listbox_files.bind('<<ListboxSelect>>', on_file_select)
listbox_files.pack()

# Create a label to show selected file info
label_file_info = tk.Label(root, text="Selected File: None")
label_file_info.pack()

# Start the main event loop
root.mainloop()
