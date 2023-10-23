from math import sqrt
from tkinter import *

from Tkinter import *


def solveAction():
    a = float(strA.get())
    b = float(strB.get())
    c = float(strC.get())
    delta = b**2 - 4*a*c
    if a == 0:
        if b == 0:
            if c == 0:
                strR.set("Vô số nghiệm")
            else:
                strR.set("Vô nghiệm")
        else:
            strR.set("x = " + str(- c / b))
    else:
        if delta > 0:
            x1 = (- b + sqrt(delta)) / (2 * a)
            x2 = (- b - sqrt(delta)) / (2 * a)
            strR.set("x1 = {0}; x2 = {1}".format(round(x1, 5), round(x2, 5)))
        elif delta == 0:
            strR.set("x1 = x2 = " + str(-b / (2 * a)))
        else:
            strR.set("Vô nghiệm")


def nextAction():
    strA.set("")
    strB.set("")
    strC.set("")
    strR.set("")


root = Tk()

strA = StringVar()
strB = StringVar()
strC = StringVar()
strR = StringVar()

root.title("PTB2")
root.resizable(height=False, width=False)
root.minsize(height=250, width=150)

Label(root,
      text="Phương trình bậc 2",
      fg="blue", font=("Tahoma", 18),
      justify=CENTER).grid(row=0, columnspan=2)

Label(root, text="Hệ số A").grid(row=1, column=0)
Entry(root, width=30, textvariable=strA).grid(row=1, column=1)

Label(root, text="Hệ số B").grid(row=2, column=0)
Entry(root, width=30, textvariable=strB).grid(row=2, column=1)

Label(root, text="Hệ số C").grid(row=3, column=0)
Entry(root, width=30, textvariable=strC).grid(row=3, column=1)

frameBtn = Frame()
Button(frameBtn, text="Giải", command=solveAction).pack(side=LEFT)
Button(frameBtn, text="Tiếp", command=nextAction).pack(side=LEFT)
Button(frameBtn, text="Thoát", command=root.quit).pack(side=LEFT)
frameBtn.grid(row=4, columnspan=2)

Label(root, text="Kết quả").grid(row=5, column=0)
Entry(root, width=30, textvariable=strR).grid(row=5, column=1)

root.mainloop()