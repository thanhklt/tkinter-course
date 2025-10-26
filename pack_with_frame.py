import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack parenting')
window.geometry('400x600')

# top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text = 'First label', background = 'red')
label2 = ttk.Label(top_frame, text = 'Label 2', background = 'blue')
label1.pack(side="left",fill="both",expand=True)
label2.pack(side="left",fill="both",expand=True)
top_frame.pack(fill="both", expand=True)

# middle widget
label3 = ttk.Label(window, text = 'Another label', background = 'green')
label3.pack(expand=True)
# bottom frame
bottom_frame = ttk.Frame(window)
left_bottom_frame = ttk.Frame(bottom_frame)
label4 = ttk.Label(left_bottom_frame, text = 'Last of the labels', background = 'orange')
button = ttk.Button(left_bottom_frame, text = 'A Button')
button2 = ttk.Button(left_bottom_frame, text = 'Another Button')
button.pack(side="left", expand=True, fill="both")
label4.pack(side="left", expand=True, fill="both")
button2.pack(side="left", expand=True, fill="both")
left_bottom_frame.pack(side="left", expand=True, fill="both")

# Exercise btn
bt3 = ttk.Button(bottom_frame, text="Button 3")
bt4= ttk.Button(bottom_frame, text= " Button 4")
bt5= ttk.Button(bottom_frame, text= "Button 5")
bt3.pack(expand=True, fill="both")
bt4.pack(expand=True, fill="both")
bt5.pack(expand=True, fill="both")

bottom_frame.pack(expand=True, fill="both",padx=20, pady=20)



# runs
window.mainloop()