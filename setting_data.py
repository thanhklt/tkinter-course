import tkinter as tk
from tkinter import ttk

# Có 2 cách lấy dữ liệu tu widget
# C1: Dung bien
# C2: Dung get() ( KO PHAI WIDGET NAO CUNG CO)

# THay dổi widget dùng config() hoac configure() hoặc var['attr']
def button_func():
    entry_text =entry.get()

    # Update label
    # label.configure(text= "Some other text")
    label["text"] = entry_text
    entry["state"] = "disabled"
    # print(label.configure())

def reset_func():
    label["text"] = "some other text"
    entry["state"] ="enabled"
# window
window = tk.Tk()
window.title("Get and set data from widget")
window.geometry("800x500")

# widgets
label = ttk.Label(master=window, text="My label")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

btn = ttk.Button(master=window, text="Click me", command=button_func)
btn.pack()

reset_btn = ttk.Button(master=window, text="Reset", command=reset_func)
reset_btn.pack()
window.mainloop()