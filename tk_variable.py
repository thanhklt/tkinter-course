import tkinter as tk
from tkinter import ttk

# Tkinter variable là những biến trong tkinter dùng để tương tác giữa các widget, lấy dữ liệu
# StringVar, IntVar, FloatVar.....
# value de chinh gt mac dinh
# Textvariable de cai moi quan he
# de lay gt hien tai dung StringVar.get()


def button_func():
    print(string_var.get())
    string_var.set("set value")


#Window
window = tk.Tk()
window.title("Tkinter Variables")
window.geometry("800x500")

# Tk variables
string_var = tk.StringVar(value= "Type in")


# Widgets
label = ttk.Label(master=window, text="Some text", textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable= string_var)
entry.pack()

entry2 = ttk.Entry(master=window, textvariable= string_var)
entry2.pack()


btn = ttk.Button(master=window, text="Click", command=button_func)
btn.pack()

exercise_var = tk.StringVar(value="test")

entry1 = ttk.Entry(master=window, textvariable=exercise_var)
entry1.pack()

entry2 = ttk.Entry(master=window, textvariable= exercise_var)
entry2.pack()

label1 = ttk.Label(master=window, text="My label", textvariable= exercise_var)
label1.pack()
# Run
window.mainloop()