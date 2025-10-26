import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('400x300')

# widgets
label1 = ttk.Label(window, text = 'Label 1', background = 'green')
label2 = ttk.Label(window, text = 'Label 2', background = 'red', width = 50)

# layout
# label1.pack()
# label2.pack(fill="x")

# Grid
window.rowconfigure((0,1), weight=1, uniform='a')
window.columnconfigure((0,1), weight=1, uniform='a')
label1.grid(row=0, column=0, stick="wens")
label2.grid(row=1, column=0)
# run
window.mainloop()