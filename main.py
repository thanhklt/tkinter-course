import tkinter as tk
from tkinter import ttk

def button_func():
    print("A button has just been pressed")

def greeting():
    print("Hello")
# Create window
window = tk.Tk()
window.title("Window and Widget")
window.geometry("800x500")

# Create widgets

# tk text
# Tham so master de xac dinh frame ma widget se hien thi ( Cha chứa con)
text = tk.Text(master=window)
text.pack()

# ttk label
label = ttk.Label(master=window, text="This is the text")
label.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# ttk button
# btn = ttk.Button(master=window, text="A button", command=button_func)
# btn.pack()

new_text = ttk.Label(master=window, text="My label")
new_text.pack()

new_btn = ttk.Button(master=window, text="btn", command=lambda: print("Hello"))
new_btn.pack()
window.mainloop()
