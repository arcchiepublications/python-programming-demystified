import tkinter as tk

def on_button_click(character):
    if character == 'C':
        display.delete(0, tk.END)
    elif character == '=':
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    else:
        display.insert(tk.END, character)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the display field
display = tk.Entry(root, justify='right')
display.grid(row=0, column=0, columnspan=4, sticky='nsew')

# List of button labels
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

# Create and place buttons
for i, button in enumerate(buttons):
    tk.Button(root, text=button, command=lambda b=button: on_button_click(b)).grid(row=i//4 + 1, column=i%4)

# Start the GUI event loop
root.mainloop()
