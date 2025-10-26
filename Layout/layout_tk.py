import tkinter as tk
from tkinter import ttk

# Setups
window = tk.Tk()
window.title("Layout in TKinter")
window.geometry("600x400")

# Widgets
label1 = ttk.Label(master= window, text="Label 1", background= "red")
# label1.pack(side="left", expand=True, fill="both")

label2 = ttk.Label(master= window, text="Label 2", background= "blue")
# label2.pack(side="left", expand=True, fill="both")

# Grid

# Setup
# window.columnconfigure(0, weight= 1)
# window.columnconfigure(1, weight= 1)
# window.columnconfigure(2, weight=2)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)
#
# label1.grid(column=1, row=0, sticky="nsew")
# label2.grid(column=1, row=1, sticky="news", columnspan=2)

# Place
label1.place(x=0, y=0, width=200, height=100)
label2.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="ne")

# Runs
window.mainloop()