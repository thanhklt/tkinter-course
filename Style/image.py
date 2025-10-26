import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# window
window = tk.Tk()
window.title('Grid')
window.geometry('600x400')

# import img
img_original = Image.open("./images/raccoon.jpg").resize(size=(600,400))
img_tk = ImageTk.PhotoImage(img_original)
# widget
# label = ttk.Label(window, text="raccoon", image=img_tk)
# label.pack()
python_dark = Image.open("./images/python_dark.png").resize(size=(30,30))
python_dark_tk = ImageTk.PhotoImage(python_dark)
button = ttk.Button(window, text="My btn", image=python_dark_tk)
button.pack()
# runs
window.mainloop()