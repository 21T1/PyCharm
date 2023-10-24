from tkinter import *


def press(c):
    global isResult

    if isResult:
        strR.set("")
    strR.set(strR.get() + str(c))

    isResult = False


def clrAction():
    strR.set("")
    global isResult
    isResult = False


def solveAction():
    try:
        result = eval(strR.get())
        strR.set(str(result))
    except:
        strR.set("Error")

    global isResult
    isResult = True


root = Tk()

strR = StringVar()
isResult = False

root.title("Simple Calculator")
root.resizable(width=False, height=False)
root.minsize(width=150, height=170)

Entry(root, width=37, textvariable=strR).grid(row=0, columnspan=3)

Button(root, text="1", command=lambda: press(1)).grid(row=1, column=0, sticky="nesw")
Button(root, text="2", command=lambda: press(2)).grid(row=1, column=1, sticky="nesw")
Button(root, text="3", command=lambda: press(3)).grid(row=1, column=2, sticky="nesw")

Button(root, text="4", command=lambda: press(4)).grid(row=2, column=0, sticky="nesw")
Button(root, text="5", command=lambda: press(5)).grid(row=2, column=1, sticky="nesw")
Button(root, text="6", command=lambda: press(6)).grid(row=2, column=2, sticky="nesw")

Button(root, text="7", command=lambda: press(7)).grid(row=3, column=0, sticky="nesw")
Button(root, text="8", command=lambda: press(8)).grid(row=3, column=1, sticky="nesw")
Button(root, text="9", command=lambda: press(9)).grid(row=3, column=2, sticky="nesw")

Button(root, text="-", command=lambda: press("-")).grid(row=4, column=0, sticky="nesw")
Button(root, text="0", command=lambda: press(0)).grid(row=4, column=1, sticky="nesw")
Button(root, text=".", command=lambda: press(".")).grid(row=4, column=2, sticky="nesw")

FrameBtn = Frame()
Button(FrameBtn, width=5, text="+", command=lambda: press("+")).pack(side=LEFT, fill=X)
Button(FrameBtn, width=5, text="-", command=lambda: press("-")).pack(side=LEFT)
Button(FrameBtn, width=5, text="*", command=lambda: press("*")).pack(side=LEFT)
Button(FrameBtn, width=5, text="/", command=lambda: press("/")).pack(side=LEFT)
Button(FrameBtn, width=5, text="=", command=solveAction).pack(side=LEFT)
FrameBtn.grid(row=5, columnspan=3)


Button(root, text="Clr", command=clrAction).grid(row=6, columnspan=3, sticky="nesw")
# disp = Entry(window, state='readonly', readonlybackground="white")
# disp.grid(column=0, row=0, columnspan=4)
# #row 1
# seven = Button(window, text="7")
# seven.grid(column=0,row=1, sticky='nesw')
#
# eight = Button(window, text="8")
# eight.grid(column=1,row=1, sticky='nesw')
#
# nine = Button(window, text="9")
# nine.grid(column=2,row=1, sticky='nesw')
#
# divide = Button(window, text="÷")
# divide.grid(column=3,row=1, sticky='nesw')
#
# window.mainloop()

root.mainloop()