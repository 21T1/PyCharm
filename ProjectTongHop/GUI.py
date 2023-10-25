from tkinter import *
from File import *


def clrAction():
    ID.set("")
    Name.set("")
    Year.set("")


def strBook(item):
    """Convert item (list) to string"""
    return "[{0}] {1} ({2})".format(item[0], item[1], item[2])


def showLstBook(lstBook):
    """Show list lstBook in listbox"""
    listbox.delete(0, END)
    for item in lstBook:
        listbox.insert(END, strBook(item))


def showLst():
    """Show list from file"""
    lstBook = readFile()
    showLstBook(lstBook)


def addAction():
    """Add new book"""
    ib = ID.get()
    nb = Name.get()
    yb = Year.get()
    if ib != "" and nb != "" and yb != "":
        book = ib + ";" + nb + ";" + yb
        writeFile(book)
        showLst()
        clrAction()


def checkStr(a, b):
    """Check if str A is not equal to null, str A is in B"""
    if a == "":
        return True
    elif a.upper() in b.upper():
        return True
    return False


def searchAction():
    """Search for book"""
    lstBook = readFile()
    listbox.delete(0, END)
    ib = ID.get()
    nb = Name.get()
    yb = Year.get()
    for item in lstBook:
        if checkStr(ib, item[0]) and checkStr(nb, item[1]) and checkStr(yb, item[2]):
            listbox.insert(END, strBook(item))


def sortAction():
    """Sort book list (year newest)"""
    lstBook = readFile()
    for i in range(len(lstBook)):
        for j in range(i, len(lstBook)):
            a = lstBook[i]
            b = lstBook[j]
            if a[2] < b[2]:
                lstBook[i] = b
                lstBook[j] = a
    showLstBook(lstBook)


root = Tk()
root.title("Quản lý sách")
root.minsize(height=300, width=300)

# variables
ID = StringVar()
Name = StringVar()
Year = StringVar()

# Title
Label(root,
      text="Quản Lý Sách",
      fg="blue", font=("Cambria", 16)
      ).grid(row=0, columnspan=2)

# List box
listbox = Listbox(root, width=50)
listbox.grid(row=1, columnspan=2)
showLst()

# Information
Label(root, text="Mã sách").grid(row=2, column=0, sticky="w")
Entry(root, width=30, textvariable=ID).grid(row=2, column=1)

Label(root, text="Tên sách").grid(row=3, column=0, sticky="w")
Entry(root, width=30, textvariable=Name).grid(row=3, column=1)

Label(root, text="Năm xuất bản").grid(row=4, column=0, sticky="w")
Entry(root, width=30, textvariable=Year).grid(row=4, column=1)

# Btn Action
Btn = Frame()
Button(Btn, text="Thêm", command=addAction).pack(side=LEFT)
Button(Btn, text="Tìm", command=searchAction).pack(side=LEFT)
Button(Btn, text="Sắp xếp", command=sortAction).pack(side=LEFT)
Button(Btn, text="Thoát", command=root.quit).pack(side=LEFT)
Btn.grid(row=5, column=1)

root.mainloop()
