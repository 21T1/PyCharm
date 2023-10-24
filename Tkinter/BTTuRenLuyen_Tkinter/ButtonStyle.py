from tkinter import *


root = Tk()


root.title("Button Style")
root.minsize(width=400, height=200)


# Label Border Width
Label(root, width=15, height=2, text="borderwidth=0").grid(row=0, column=0)
Label(root, width=15, height=2, text="borderwidth=1").grid(row=1, column=0)
Label(root, width=15, height=2, text="borderwidth=2").grid(row=2, column=0)
Label(root, width=15, height=2, text="borderwidth=3").grid(row=3, column=0)
Label(root, width=15, height=2, text="borderwidth=4").grid(row=4, column=0)


# Btn Raised
BtnRaised = Frame()
Button(BtnRaised, width=10, text="raised", bd=0, relief=RAISED).pack(side=TOP, pady=7)
Button(BtnRaised, width=10, text="raised", bd=1, relief=RAISED).pack(side=TOP, pady=5)
Button(BtnRaised, width=10, text="raised", bd=2, relief=RAISED).pack(side=TOP, pady=5)
Button(BtnRaised, width=10, text="raised", bd=3, relief=RAISED).pack(side=TOP, pady=5)
Button(BtnRaised, width=10, text="raised", bd=4, relief=RAISED).pack(side=TOP, pady=5)
BtnRaised.grid(row=0, column=1, rowspan=10)


# Btn Sunken
BtnSunken = Frame()
Button(BtnSunken, width=10, text="sunken", bd=0, relief=SUNKEN).pack(side=TOP, pady=7)
Button(BtnSunken, width=10, text="sunken", bd=1, relief=SUNKEN).pack(side=TOP, pady=5)
Button(BtnSunken, width=10, text="sunken", bd=2, relief=SUNKEN).pack(side=TOP, pady=5)
Button(BtnSunken, width=10, text="sunken", bd=3, relief=SUNKEN).pack(side=TOP, pady=5)
Button(BtnSunken, width=10, text="sunken", bd=4, relief=SUNKEN).pack(side=TOP, pady=5)
BtnSunken.grid(row=0, column=2, rowspan=10)


# Btn Flag
BtnFlat = Frame()
Button(BtnFlat, width=10, text="flat", bd=0, relief=FLAT).pack(side=TOP, pady=7)
Button(BtnFlat, width=10, text="flat", bd=1, relief=FLAT).pack(side=TOP, pady=5)
Button(BtnFlat, width=10, text="flat", bd=2, relief=FLAT).pack(side=TOP, pady=5)
Button(BtnFlat, width=10, text="flat", bd=3, relief=FLAT).pack(side=TOP, pady=5)
Button(BtnFlat, width=10, text="flat", bd=4, relief=FLAT).pack(side=TOP, pady=5)
BtnFlat.grid(row=0, column=3, rowspan=10)


# Btn Ridge
BtnRidge = Frame()
Button(BtnRidge, width=10, text="ridge", bd=0, relief=RIDGE).pack(side=TOP, pady=7)
Button(BtnRidge, width=10, text="ridge", bd=1, relief=RIDGE).pack(side=TOP, pady=5)
Button(BtnRidge, width=10, text="ridge", bd=2, relief=RIDGE).pack(side=TOP, pady=5)
Button(BtnRidge, width=10, text="ridge", bd=3, relief=RIDGE).pack(side=TOP, pady=5)
Button(BtnRidge, width=10, text="ridge", bd=4, relief=RIDGE).pack(side=TOP, pady=5)
BtnRidge.grid(row=0, column=4, rowspan=10)


# Btn Groove
BtnGroove = Frame()
Button(BtnGroove, width=10, text="groove", bd=0, relief=GROOVE).pack(side=TOP, pady=7)
Button(BtnGroove, width=10, text="groove", bd=1, relief=GROOVE).pack(side=TOP, pady=5)
Button(BtnGroove, width=10, text="groove", bd=2, relief=GROOVE).pack(side=TOP, pady=5)
Button(BtnGroove, width=10, text="groove", bd=3, relief=GROOVE).pack(side=TOP, pady=5)
Button(BtnGroove, width=10, text="groove", bd=4, relief=GROOVE).pack(side=TOP, pady=5)
BtnGroove.grid(row=0, column=10, rowspan=10)

# Btn Solid
BtnSolid = Frame()
Button(BtnSolid, width=10, text="solid", bd=0, relief=SOLID).pack(side=TOP, pady=7)
Button(BtnSolid, width=10, text="solid", bd=1, relief=SOLID).pack(side=TOP, pady=5)
Button(BtnSolid, width=10, text="solid", bd=2, relief=SOLID).pack(side=TOP, pady=5)
Button(BtnSolid, width=10, text="solid", bd=3, relief=SOLID).pack(side=TOP, pady=5)
Button(BtnSolid, width=10, text="solid", bd=4, relief=SOLID).pack(side=TOP, pady=5)
BtnSolid.grid(row=0, column=6, rowspan=10)


root.mainloop()