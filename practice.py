#BT1: Tạo 1 text, 1 entry, 1 button. Khi thay đổi entry thì nội dung text và button cũng bị thay đổi. Nếu ấn button thì
#nội dung được chỉnh thành new_value.

import tkinter as tk
from tkinter import ttk

# Func
def btn_func():
    string_var.set("new_value")

#Window
window = tk.Tk()
window.title("Practice")
window.geometry("800x500")

# TK vars
string_var = tk.StringVar(value="Original value")

#Widget
label = ttk.Label(master= window, text="Label", textvariable= string_var)
label.pack()

entry = ttk.Entry(master= window, textvariable= string_var)
entry.pack()

btn = ttk.Button(master= window, text="Button", textvariable= string_var, command= btn_func)
btn.pack()
window.mainloop()