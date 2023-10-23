from tkinter import *


def addAction():
    a = float(strA.get())
    b = float(strB.get())
    strR.set(str(a + b))


def subAction():
    a = float(strA.get())
    b = float(strB.get())
    strR.set(str(a - b))


def mulAction():
    a = float(strA.get())
    b = float(strB.get())
    strR.set(str(a * b))


def divAction():
    a = float(strA.get())
    b = float(strB.get())
    strR.set(str(a / b))


root = Tk()

strA = StringVar()
strB = StringVar()
strR = StringVar()

root.title("Cộng Trừ Nhân Chia")
root.resizable(height=False, width=False)
root.minsize(width=200, height=250)

Label(root, text="Cộng Trừ Nhân Chia",
      fg="red", font=("Tahoma", 20)).grid(row=0, columnspan=3)

frameBtn = Frame(root)
Button(frameBtn, text="Cộng", command=addAction).pack(side=TOP, fill=X)
Button(frameBtn, text="Trừ", command=subAction).pack(side=TOP, fill=X)
Button(frameBtn, text="Nhân", command=mulAction).pack(side=TOP, fill=X)
Button(frameBtn, text="Chia", command=divAction).pack(side=TOP, fill=X)
frameBtn.grid(row=1, column=0, rowspan=4)

Label(root, text="Số a:").grid(row=1, column=1)
Entry(root, width=15, textvariable=strA).grid(row=1, column=2)

Label(root, text="Số b:").grid(row=2, column=1)
Entry(root, width=15, textvariable=strB).grid(row=2, column=2)

Label(root, text="Kết quả:").grid(row=3, column=1)
Entry(root, width=15, textvariable=strR).grid(row=3, column=2)

Button(root, text="Thoát", command=root.quit).grid(row=4, column=2)

root.mainloop()