1/ Các widget đã học ( LUON PHAI TRUYEN MASTER DAU TIEN):
- Của tk
    + text
- Của ttk
    + entry
    + label
    + btn
    + check btn (variable, onvalue, offvalue)
    + radio btn (cac nut phai co value khac nhau)
    + common box (values = list): giống select cua html, widget có thêm event <<ComboboxSelected>>"
    + spinbox(from_ , to, increment=<buoc nhay>, command, textvariable), widget có thêm event <<Increment>>, <<Decrement>>

    + treeview aka table
        Treeview(columns=(....), show="headings")
        Để add tên cột xuất ra phải map col_val -> gt xuất ra = table.heading("col-val", text="text name")
        Để insert gt dùng table.insert(parent, index=tk.END, values=())
        Mỗi items trong bảng có 1 gt khác nhau. để lấy dùng bind("<<TreeviewSelect", table.selection()) và
        table.item(obj) để lấy thông tin hàng
        table.delete(obj) để xóa hàng

    + frame: Mot cua so nho trong giao dien window, dung de tao bo cuc phuc tap
*** LƯU Ý***
- 3 cách để tha  n y đổi thuộc tính 1 widget
- variable: để lưu thông tin vào
- textvariable: để đưa gt biến ra widget  n 

2/ Tk variable
- tk.StringVar(value=<gt mac dinh>)
- Để lấy gt dùng get(), sửa dùng set()

3/ Bind event
- widget.bind(<event-str>, func)
