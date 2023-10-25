from tkinter import *


def showResult():
    F = float(strF.get())
    C = (F - 32) * 5/9
    strR.set(str(C))


root = Tk()
root.title("Chuyển độ F thành độ C")
root.minsize(width=150, height=100)

strF = StringVar()
strR = StringVar()

Label(root, text="Nhập độ F:").grid(row=0, column=0)
Entry(root, width=20, textvariable=strF).grid(row=0, column=1)

Button(root, text="Chuyển đổi", command=showResult).grid(row=1, column=1, sticky="news", pady=10)

Label(root, text="Độ C:").grid(row=2, column=0)
Entry(root, width=20, textvariable=strR).grid(row=2, column=1)

root.mainloop()