from tkinter import *


def solveAction():
      a = float(strA.get())
      b = float(strB.get())
      if a == 0:
            if b == 0:
                  strR.set("Vô số nghiệm")
            else:
                  strR.set("Vô nghiệm")
      else:
            strR.set(str(-b/a))


def nextAction():
      strA.set("")
      strB.set("")
      strR.set("")


root = Tk()

strA = StringVar()
strB = StringVar()
strR = StringVar()


root.title("PTB1")
root.minsize(height=130, width=250)
root.resizable(height=True, width=True)

Label(root,
      text="Phương Trình Bậc 1",
      fg="red", font=("Tahoma", 16),
      justify=CENTER
      ).grid(row=0, columnspan=2)

Label(root, text="Hệ số a:").grid(row=1, column=0)
Entry(root, width=30, textvariable=strA).grid(row=1, column=1)

Label(root, text="Hệ số b:").grid(row=2, column=0)
Entry(root, width=30, textvariable=strB).grid(row=2, column=1)

frameButton = Frame()
Button(frameButton, text="Giải", command=solveAction).pack(side=LEFT)
Button(frameButton, text="Tiếp", command=nextAction).pack(side=LEFT)
Button(frameButton, text="Thoát", command=root.quit).pack(side=LEFT)
frameButton.grid(row=3, columnspan=2)

Label(root, text="Kết quả:").grid(row=4, column=0)
Entry(root, width=30, textvariable=strR).grid(row=4, column=1)


root.mainloop()
