import tkinter as tk
from tkinter import ttk

# Setup
window = tk.Tk()
window.title("Common box and spinbox")
window.geometry("600x400")

# Combobox
items = ("Ice cream", "Pizza", "Hamburger")
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_string)
combo["values"] = items
combo.pack()

# Spinbox
spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(window, from_=3, to= 20, increment=3, command= "A arrow was pressed", textvariable=spin_int)
spin.bind("<<Increment>>", lambda event: print("Go up"))
spin.bind("<<Decrement>>", lambda event: print("Go down"))
# spin["values"] = (1,2,3,4,5,
spin.pack()

# Exercise
spin_value = ("A", 'B', 'C', 'D', 'E')
exer_var = tk.StringVar(value= spin_value[0])
spin_ex = ttk.Spinbox(window, textvariable= exer_var)
spin_ex["values"] = spin_value

# Event
spin_ex.bind("<<Decrement>>", lambda event: print(exer_var.get()))
spin_ex.pack()

#Events
combo.bind("<<ComboboxSelected>>", lambda e: combo_label.configure(text= food_string.get()))

combo_label = ttk.Label(window, text="A label")
combo_label.pack()

# Runs
window.mainloop()