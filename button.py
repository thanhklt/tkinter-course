# # Co 3 loai btn trong tkinter
# Button
# Check btn
# Radio btn
# Bat buoc phai su dung tkinter variable neu muon dung dung

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Buttons")
window.geometry("600x400")

# Btn

button_string = tk.StringVar(value="A button with string var")
def button_func():
    print("A basic button")
button = ttk.Button(window, text="A simple button", command= button_func, textvariable= button_string)
button.pack()

# Check btn
# De luu chu gt cua check btn can tao 1 bien
# Textvar dung de dat gt text cua widget con var dung de lay gt cua widget
# Ban chat tk var la kdl nguyen thuy nhung dc dat trong vung nho phuc tap hon
check_var = tk.IntVar(value=10)
check = ttk.Checkbutton(window, text="Checkbox1", command= lambda :print(check_var.get()),
                        variable= check_var,
                        onvalue=10, # GT tra ve khi bat, neu gt khoi tao = thi se checkbox truoc
                        offvalue=5) # GT tra ve khi tat
check.pack()

# Radio buttons
# Y tuong cua radio button la co nhieu radio nhung chi co the chon 1 nut. Gt nut se dc xai chung 1 bien
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window, text="Radio button 1", value="radio1", command= lambda: print(radio_var.get()), variable= radio_var) # Khi tao radio button phai luon co value
radio1.pack()

radio2 = ttk.Radiobutton(window, text="Radio button 2", value=2, command= lambda: print(radio_var.get()), variable= radio_var)
radio2.pack()


#Exercise
#Check
check_btn_var = tk.BooleanVar(value=True)
check_btn = ttk.Checkbutton(window, text="A button", onvalue=True, offvalue=False, variable=check_btn_var, command=lambda: print(radio_btn_var.get()))
check_btn.pack()
# Radio btn
def radio_func():
    print(check_btn_var.get())
    check_btn_var.set(False)
radio_btn_var = tk.StringVar()
radio_btn1 = ttk.Radiobutton(window, text="First radio btn", value="A", command=radio_func, variable= radio_btn_var)
radio_btn1.pack()

radio_btn2 = ttk.Radiobutton(window, text="Second radio btn", value="B", command=radio_func, variable=radio_btn_var)
radio_btn2.pack()


window.mainloop()
