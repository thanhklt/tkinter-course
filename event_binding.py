import tkinter as tk
from tkinter import ttk

# De bind su dung: widget.bind(event, func). Format cua event la: modifier-type-detail ( Alt-Keypress-a)
# tk chi kiem tra event tren widget duoc bind
def get_pos(event):
    print(f"x={event.x}, y={event.y}")
#Setup
window = tk.Tk()
window.title("Event binding")
window.geometry("800x600")

#Widgets
text= tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text="click me")
button.pack()

text.bind("<Shift-MouseWheel>", lambda e: print("Mouse wheel"))
#Events
# Khi event kich hoat, tk tu truyen 1 tham so vao func
button.bind("<Alt-KeyPress-a>", lambda event: print(event))
# window.bind("<Motion>", get_pos)
# window.bind("<KeyPress>", lambda event: print(f"A button ({event.char})has been pressed"))
# entry.bind("<FocusIn>", lambda event: print("A entry is selected"))
# Run
window.mainloop()

