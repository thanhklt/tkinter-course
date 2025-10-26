import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Grid')
window.geometry('600x400')

# widgets
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Label 3', background = 'green')
label4 = ttk.Label(window, text = 'Label 4', background = 'yellow')
button1 = ttk.Button(window, text = 'Button 1')
button2 = ttk.Button(window, text = 'Button 2')
entry = ttk.Entry(window)

# define a grid
window.rowconfigure(0, weight=1, uniform='a')
window.rowconfigure(1, weight=1, uniform='a')
window.rowconfigure(2, weight=1, uniform='a')
window.rowconfigure(3, weight=3, uniform='a')
window.columnconfigure((0,1,2), weight=1, uniform='a')
window.columnconfigure(3, weight=2, uniform='a')

# widgets
label1.grid(row=0, column=0, sticky="news")
label2.grid(row=0, column=2, sticky="news")
label2.grid(row=1, column=1,rowspan=3, sticky="news")
label3.grid(row=1, column=0,columnspan=3, sticky="wens", padx=20, pady=10)
label4.grid(row=3, column=3,sticky="se")

# Exercise widgets
var = tk.StringVar(value="default")

btn1 = ttk.Button(window, text="Button 1", textvariable=var)
entry = ttk.Entry(window, textvariable=var)
btn2 = ttk.Button(window, textvariable=var)
btn2.grid(row=2, column=2, sticky="news")
btn1.grid(row=0, column=3, sticky="news")
entry.grid(row=3, column=3)
# runs
window.mainloop()