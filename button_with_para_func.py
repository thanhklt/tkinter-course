import tkinter as tk
from tkinter import ttk

# De truyen tham so vao trong ham truyen vao btn
# C1: Dung ham lambda lambda: btn_func(str)
# C2: Ham tra ve ham
def btn_func(entry_str):
    print("A button has been pressed")
    print(f"Value: {entry_str.get()}")

def outer_func(para):
    def inner_func():
        print("A button has been pressed")
        print(f"Value: {para.get()}")
    return inner_func
#Setup
window = tk.Tk()
window.title("Button with parameter func")
window.geometry("800x600")

#Widgets
entry_var = tk.StringVar(value="test")
entry = ttk.Entry(window, textvariable= entry_var)
entry.pack()

button = ttk.Button(window, text="A button", command=outer_func(entry_var)) # Chu y get trong func va get o day la 2 cai khac nhau
button.pack()


#Run
window.mainloop()
