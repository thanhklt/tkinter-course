import tkinter as tk
from tkinter import ttk
from random import choice

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

# data
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

# Treeview
table = ttk.Treeview(window, columns=("first", "last", "email"), show="headings")
table.heading("first", text="First name")
table.heading("last", text="Sure name")
table.heading("email", text="Email")

# Insert value into tbl
for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    table.insert(parent="", index=0, values=(first, last, f"{first}{last}@gmail.com"))

table.insert(parent="", index= tk.END, values=("XXX","YYY","ZZZ"))

table.pack(fill="both", expand=True)

# Events
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i))
table.bind("<<TreeviewSelect>>",item_select)

def delete_item(_):
    delete_obj = table.selection()
    for i in table.selection():
        table.delete(i)
    print("Xóa đối tượng thành công")
table.bind("<Delete>", delete_item)
# Items

# run
window.mainloop()