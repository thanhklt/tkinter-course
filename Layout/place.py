import tkinter as tk
from tkinter import ttk

# Setup
window = tk.Tk()
window.geometry("400x600")
window.title("Place layout")

# Widgets
label1 = ttk.Label(window, text="Label 1", background="red")
label2 = ttk.Label(window, text="Label 2", background="blue")
label3 = ttk.Label(window, text="Label 3", background="green")
btn = ttk.Button(window, text="Button 1")

# Layout
label1.place(x=300, y= 100, width=100, height=200)
label2.place(relx=0.2, rely=0.1, relwidth=0.4, relheight=0.5)
label3.place(x=80, y=60, width=160, height=300)
btn.place(relx=1, rely=1, anchor="se")

# Frame
frame = ttk.Frame(window)
label_frame = ttk.Label(frame, text="Frame label", background="yellow")
btn_frame = ttk.Button(frame, text= "Frame button")

# Frame layout
frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
label_frame.place(relx=0, rely=0, relwidth=1, relheight=0.5)
btn_frame.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# Exercise
exercise_label = ttk.Label(window, text="Exercise label", background="purple")
exercise_label.place(relx=0.5, rely=0.5, relwidth=0.5, height=200, anchor="center")
# Run
window.mainloop()